#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 10:08:03 2023

@author: alain
"""

#from geonodes.core.socket import DataSocket
#from geonodes.core.node import Node
#from geonodes.core.tree import Tree

from geonodes.nodes import nodes

# ====================================================================================================
# Simulation zone

class Simulation:
    """ Simulation zone
    
    This class Simulation generates the two nodes of a simulation zone: simulation input and output nodes.
    The simulation exposes as class attributes the geometry and the simulation variables used in the simulation zone.
    
    The key of the keyword arguments is used to name the sockets of the input and outpout node.
        
    ``` python
    simul = Simulation(geometry=mesh, speed=(0, 0, 0))
    simul.geometry  # The geometry within the simulation zone
    simul.speed     # The speed within the simulation zone
    ``` 
        
    When the simulation loop is terminated, the changes on the simulation variables must be connected to
    the output nodes : ` simul.output.geometry = simul.geometry `. This is done automatically with the 'close' method :
        
    ``` python
    simul = Simulation(geometry=mesh, speed=(0, 0, 0))
    simul.geometry.faces.shade_smooth = True
    simul.speed += (0, 0, 1)
    simul.close()
    ```
    
    Bettter use the context manager through a `with` statement:
        
    ``` python
    with gn.Simulation(geometry=mesh, speed=(0, 0, 0)) as simul:
        simul.geometry.faces.shade_smooth = True
        simul.speed += (0, 0, 1)
    ```
    
    Once the simulation is closed, the variables are the output sockets of the simulation output node.
    They can be used to get the result of a simulation step:
        
    ``` python
    with gn.Simulation(geometry=mesh) as simul:
        # simul.geometry refers to the geometry inside the simulation zone
        simul.geometry.faces.shade_smooth = True
        
    # Outside the simulation zone, the geometry refers to the result of the simulation
    # Let's connect the result of the simulation to the output of the tree
    tree.og = simul.geometry
    ``` 
    
    Args:
    - **kwargs : variables to use within the loop. Each key word creates a variable accessible within the simulation step
      and, once the simulation closed, as the result of the simulation.
    """
    
    def __init__(self, **kwargs):
        
        import geonodes as gn
        
        # ----- Create an link the input and output simulation nodes
        
        self.input  = nodes.SimulationInput()
        self.output = nodes.SimulationOutput()
        self.input.bnode.pair_with_output(self.output.bnode)
        
        # ----- Create the simulation state items
        # Geometry socket is created by default, it is first deleted
        
        self.output.bnode.state_items.clear()
        types = {}
        
        for name, value in kwargs.items():
            typ = None
            
            if isinstance(value, bool):
                socket = gn.Boolean(value)
            elif isinstance(value, int):
                socket = gn.Integer(value)
            elif isinstance(value, float):
                socket = gn.Float(value)
            elif isinstance(value, str):
                socket = gn.String(value)
            elif isinstance(value, tuple):
                socket = gn.Vector(value)
            else:
                socket = value
                typ = type(value)
                
            self.output.bnode.state_items.new(socket_type=socket.base_data_type, name=name.capitalize())
            types[name] = typ
            
        # ----- Update in and out sockets dynamically created
        
        self.input.update_inout_sockets()
        self.output.update_inout_sockets()
        
        # ----- Sockets types
        
        for name, typ in types.items():
            if typ is not None:
                self.input.outsockets_classes[name]  = typ
                self.output.outsockets_classes[name] = typ
                
        # ----- Plug the values to the simulation input node
        
        for name, value in kwargs.items():
            self.input.set_input_socket(name.lower(), value)
        
        # ----- Output sockets of the input node
        # Once the simulation is closed, these attrs will change
        
        for name in self.input.outsockets:
            setattr(self, name, self.input.get_output_socket(name))
            
        # ----- Just for tracking
        
        self.closed = False
        
        
    # ====================================================================================================
    # Context manager
    
    def close(self):
        """ Closing the simulation zone.
        
        Two operations are performed when "closing" a simulation zone:
        - connect the simulation variales to the input sockets of the output node
        - map the corresponding variables of the Simulation instance to the output sockets of the output node
        
        Basically, this correspond to this pseudo code:
        ``` python
        simul.output.geometry = simul.geometry # connect simul.geometry to the input socket of output node
        simul.geometry = simul.output.geometry # simul.gemetry points now to the output socket of output node
        ```
        
        In addition, the 'delta_time' attribute is deleted to avoid use outside the simulation.
        """
        
        if self.closed:
            return
        
        # ----- Connect the input sockets of the output node
        
        for name in self.output.outsockets:
            self.output.set_input_socket(name, getattr(self, name))

        # ----- Now that the simulation is closed, accessing the variables is from the output socket:
            
        for name in self.output.outsockets:
            setattr(self, name, self.output.get_output_socket(name))
            
        delattr(self, 'delta_time')
            
        
    def __enter__(self):
        return self
    
    def __exit__(self, exception_type, exception_value, traceback):
        self.close()

    # ====================================================================================================
    # Utitlity
            
    def __str__(self):
        sclosed = "CLOSED" if self.closed else "OPEN"
        vs = list(self.input.insockets.keys())
        vs[0] += f" ({self.output.outsockets_classes['geometry'].__name__})"
        s = ", ".join(vs)
        return f"<Simulation zone ({sclosed}) : {s}>"
            
    # ----------------------------------------------------------------------------------------------------
    # Create paths for trajectories
    
    @classmethod
    def Trajectories(cls, simul, count=10):
        """ This constructor build a simulation zone building curves tracking points of another simulation zone.
        
        Args:
            - simul (Simulation) : the simulation zone having a geometry of type Points
            - count (int=10) : the number of frames to use for tracking
        """
        
        import geonodes as gn
        
        tree = gn.Tree.TREE
        
        with tree.layout("POINTS TRAJECTORIES"):
            
            # ----- Points connected to the input socket Geometry of the simulation input node
            
            init_points = gn.Points(simul.input.inputs[0].connected_sockets()[0])
            
            # ----- Points connected to the input socket Geometry of the simulation output node
            # These points have the final position
            
            points = gn.Points(simul.output.inputs[0].connected_sockets()[0])

            with tree.layout("One spline instance per point"):
                curve = gn.Curve.Line(start=0, end=0).resample(count=count)
                insts = init_points.instance_on_points(instance=curve)
                insts.insts.store_named_attribute(name="temp", value=(0, 0, 0))
                
                splines = insts.realize()
                
            with tree.layout("Curves simulation"):
                
                with gn.Simulation(splines=splines, instances=insts) as sim:
                
                    # ----- Shift splines points position
                    
                    with tree.layout("Shift points position"):
                        old_locs = sim.splines.points.sample_index(value=sim.splines.points.position, index=sim.splines.points.index + 1)
                        sim.splines.points.position = old_locs
            
                    # ----- Points new positions
                        
                    with tree.layout("Update position of last points"):
                        
                        locs = cloud.points.sample_index(value=cloud.points.position)
                        sim.instances.insts.store_named_attribute(name="temp", value=locs)
                        
                        curve = sim.instances.realize()
                        locs = curve.points.sample_index(value=curve.points.named_vector("temp"))
                        
                        sim.geometry.points[(sim.geometry.points.index % count).to_integer().equal(count-1)].position = locs
            
            return sim
        
    # ====================================================================================================
    # Fluid simulation
    
    @classmethod
    def Fluid(cls, cloud, velocity=0, life=50, setup={}, acceleration={}, finish={}):
        """ Constructor building a basic simulation zone for fluid simulation.
        
        **Note**: the name of the geometry is '*cloud*'. Use ``` simul.cloud ``` to access to the points animated by the simulation.
        
        The nodes generated perform the standard operations:
        - add new points at each step
        - delete points older thant the life parameter
        - update the velocity with the acceleration
        - update the particles position with the updated velocity
            
        The acceleration nodes are generated through functions passed as argument.
        An template of the acceleration function must be:
            
        ``` python
        def gen(simul):
        ```
        
        The following example build a simple simulation from a mesh, with random initial speed and a gravity.
            
        ``` python
        import geonodes as gn
        
        with gn.Tree("Fluid", auto_capture=False) as tree:
            
            # Input geometry is supposed to be a mesh
            
            mesh = gn.Mesh(tree.ig)
            
            # Generate points on the surface
            
            points = mesh.faces.distribute_points(10).points
            
            # Random speed
            
            velocity = gn.Vector.Random((-1, -1, -1), (1, 1, 1), seed=tree.frame)
            
            # Fluid simulation with gravity
            
            simul = gn.Simulation.Fluid(points, velocity, 50, 
                acceleration=gn.Simulation.func_gravity((0, 0, -10)),
                )
            
            tree.og = mesh + simul.cloud 
        ```
        
        Simulation offers basic acceleration functions:
        - func_gravity      : constant acceleration
        - func_turbulence   : noisy acceleration
        - func_viscosity    : acceleration decreasing the speed
        - func_repulsion    : repulsion from the nearest particle
        - func_attraction   : attraction / repulsion from a location
        - func_surface_flow : acceleration along a surface slope
        - func_bounce       : bounce on a surface
        - func_group        : use a custom group to perform computations inside the simulation loop
            
        Custom nodes can be added at the begining and at the end of the simulation step with the arguments **setup** and **finish**.
        
        The same process is used to generate complementory nodes for the set up and the finalization of the zone.
        
        For instance, the following simulation simulates a fluid flowing on a surface:
            
        ``` python
        import geonodes as gn
        
        with gn.Tree("Flow", auto_capture=False) as tree:
        
            # The surface on which fluid will flow
        
            mesh = gn.Mesh(tree.ig)
            
            # Particles generation with null initial speed
            
            points   = mesh.faces.distribute_points(density=.1, seed=tree.frame).points
            velocity = gn.Vector()
            
            # Simulation with flow with viscosity and repulsion
            # Finish by making sure the particles stay on the surface and killing outside particles
            
            simul = gn.Simulation.Fluid(points, velocity, 30, 
                acceleration={
                'flow'      : gn.Simulation.func_surface_flow(mesh, gravity=(0, 0, -10)),
                'viscosity' : gn.Simulation.func_viscosity(.2),
                'repulsion' : gn.Simulation.func_repulsion(.2),
                },
                finish = {
                'stick'     : gn.Simulation.func_stick_on_surface(mesh, kill_outside=True),
                }
            )
            
            # Mesh and particles
            
            tree.og = mesh + simul.cloud
        ```
        
        Args:
            - cloud (Points): the points generated at each steap
            - velocity (Vector) : the points velocity
            - life (Integer) : particles life
            - setup (dict or function) : function generating setup nodes or dict of such functions
            - acceleration (dict or function) : function generating acceleration nodes or dict of such functions
            - finish (dict or function) : function generating finalization nodes or dict of such functions
        """
        
        import geonodes as gn
        
        tree = cloud.node.tree
        
        # ----------------------------------------------------------------------------------------------------
        # Simulation zone
        
        cloud.points.store_named_vector("velocity", velocity)
        cloud.points.store_named_integer("age", 0)

        with cls(cloud=cloud) as simul:
            
            # ----- Set up
            
            if isinstance(setup, dict):
                for stu_name, stu in setup.items():
                    with tree.layout(f"Set up: {stu_name}"):
                        stu(simul=simul) #   , cloud=simul.cloud, velocity=s_velocity, age=s_age)
                        
            else:
                with tree.layout(f"Set up"):
                    setup(simul=simul)  #, cloud=simul.cloud, velocity=s_velocity, age=s_age)
            
            # ----- Update the age, remove old particles
            
            with tree.layout("Update the age and remove old particles"):
                
                age = simul.cloud.named_integer("age") + 1
                simul.cloud.points.store_named_integer("age", age)
                simul.cloud.points[age.greater_than(life)].delete()
                
            # ----- New points with random velocity
                
            with tree.layout("Create new points with their velocity"):
                simul.cloud = gn.Points(simul.cloud + cloud)
        
            # ----- Accelerations
                
            if isinstance(acceleration, dict):
                a = gn.Vector((0, 0, 0))
                for acc_name, acc in acceleration.items():
                    with tree.layout(f"Acceleration: {acc_name}"):
                        a += acc(simul=simul) 
                        
            else:
                with tree.layout(f"Acceleration"):
                    a = acceleration(simul=simul) 
        
            # ----- Update velocities and postions
                    
            with tree.layout("Update velocity and positions"):
                vel     = simul.cloud.points.named_vector("velocity")
                new_vel = vel + a.scale(simul.delta_time)
                simul.cloud.points.position_offset = (vel + new_vel).scale(simul.delta_time/2)
                simul.cloud.points.store_named_vector("velocity", new_vel)
                
            # ----- Finishing
            
            if isinstance(finish, dict):
                for fin_name, fin in finish.items():
                    with tree.layout(f"Finish: {fin_name}"):
                        fin(simul=simul)
                        
            else:
                with tree.layout(f"Finish"):
                    finish(simul=simul) 
        
        return simul
    
    # ====================================================================================================
    # Accelerations
    
    # ----------------------------------------------------------------------------------------------------
    # A constant acceleration
    
    @staticmethod
    def func_gravity(gravity=(0, 0, -10)):
        """ Returns a function which builds a constant acceleration.
        
        The function returned by this method can be used as an argument in a simulation zone creation method:
        
        ``` python    
        simul = gn.Simulation.Fluid(acceleration=gn.Simulation.func_gravity(...))    
        ```
        
        or, if more than one acceleration function is required
        
        ``` python
        simul = gn.Simulation.Fluid(acceleration={'gravity': gn.Simulation.func_gravity(...)})
        ```
        
        Args:
            - gravity (Vector) : the gravity vector
        
        Returns:
            - function(**kwargs) : nodes generator
        """
        
        import geonodes as gn
        
        return lambda simul: gn.Vector(gravity)
    
    # ----------------------------------------------------------------------------------------------------
    # Noisy turbulence
    
    @staticmethod
    def func_turbulence(intensity=1, scale=.2, offset=(0, 0, 0), w=0.):
        """ Returns a function which builds a turbulencce for acceleration.
        
        The turbulence makes use of a 'Noise 4D' texture initialized with the function arguments.
        
        The function returned by this method can be used as an argument in a simulation zone creation method:
        
        ``` python    
        simul = gn.Simulation.Fluid(acceleration=gn.Simulation.func_turbulence(...))    
        ```
        
        or, if more than one acceleration function is required
        
        ``` python
        simul = gn.Simulation.Fluid(acceleration={
            'gravity'   : gn.Simulation.func_gravity(),
            'turbulence': gn.Simulation.func_turbulence(...),
            })
        ```
        
        Args:
            - intensity (Float) : intensity of the turbulence
            - scale (Float) : scale of Noise node
            - offset (Vector) : offset to apply in the 'Vector' socket of the noise node
            - w (Float) : value of the 'W' socket of the noise node
        
        Returns:
            - function(**kwargs) : nodes generator
        """
        
        import geonodes as gn
        
        def gen(simul):
            cloud = simul.cloud
            tree = cloud.node.tree
            return gn.Vector(gn.Texture.Noise4D(vector=cloud.points.position + offset, scale=scale, w=w).color).map_range(.5).scale(intensity)
        
        return gen
    
    # ----------------------------------------------------------------------------------------------------
    # Viscosity
    
    @staticmethod
    def func_viscosity(intensity=1, exponent=2):
        """ Returns a function which builds an acceleration simulating viscosity.
        
        The viscosity is a function of the velocity: ``` acc = -intensitty * speed**exponent ```
    
        This raw formula can return an acceleration which accelerates the particle in the other direction.
        To avoid this behavior, the acceleration norm is capped to ``` speed/delta_time ```.
        
        The function returned by this method can be used as an argument in a simulation zone creation method:
        
        ``` python    
        simul = gn.Simulation.Fluid(acceleration=gn.Simulation.func_viscosity(...))    
        ```
        
        or, if more than one acceleration function is required
        
        ``` python
        simul = gn.Simulation.Fluid(acceleration={
            'gravity'   : gn.Simulation.func_gravity(),
            'viscosity' : gn.Simulation.func_viscosity(...),
            })
        ```
        
        Args:
            - intensity (Float) : intensity of the viscosity
            - exponent (Float) : exponent parameter of the acceleration
        
        Returns:
            - function(**kwargs) : nodes generator
        """
        
        import geonodes as gn
    
        def gen(simul):
            
            velocity = simul.cloud.points.named_vector("velocity")
    
            # ----- Velocity norm
    
            n_vel = velocity.length
            
            # ----- acceleration norm
            
            a = intensity*n_vel**exponent
            
            # ----- Cap and smooth the viscosity
            
            a_max = n_vel/simul.delta_time
            a = a.map_range_smooth(0, a_max, 0, a_max)
            
            # ----- Return the acceleration
            
            return velocity.scale(-a/n_vel)
        
        return gen
    
    # ----------------------------------------------------------------------------------------------------
    # Repulsion
    
    @staticmethod
    def func_repulsion(intensity=1, exponent=2, d_min=.1, d_max=1):
        """ Returns a function which builds a repulstion acceleration with the nearest particle.
        
        The repulsion is base on the vector between the particle and its nearest neighbor.
        The acceleration is computed with the formula: ``` a = intensity * distance**(-exponent) ```
        
        To avoid division by zero, distance is minimized by the argument d_min.
        The repulsion is null when the distance is greater thant d_max
        
        The function returned by this method can be used as an argument in a simulation zone creation method:
        
        ``` python    
        simul = gn.Simulation.Fluid(acceleration=gn.Simulation.func_repulsion(...))    
        ```
        
        or, if more than one acceleration function is required
        
        ``` python
        simul = gn.Simulation.Fluid(acceleration={
            'gravity'   : gn.Simulation.func_gravity(),
            'repulsion' : gn.Simulation.func_repulsion(...),
            })
        ```
        
        Args:
            - intensity (Float) : intensity of the repulstion
            - exponent (Float) : exponent parameter of the acceleration
            - d_min (Float) : minimum distance to avoid infinite acceleration
            - d_max (Float) : repulsion maximum distance
        
        Returns:
            - function(**kwargs) : nodes generator
        """    
        
        import geonodes as gn
        
        def gen(simul):
            
            cloud = simul.cloud
            
            # ----- Index of nearest
            
            index = cloud.points.index_of_nearest(position=cloud.points.index).index
            
            # ----- Vector between the particle and its nearest neighbor
            
            v = cloud.points.position - cloud.points.sample_index(cloud.points.position, index=index)
            
            # ----- Distance
            
            d = v.length
            
            # ----- Acceleration computed on the capped distance
            
            base = gn.max(d, d_min)
            a = -intensity*base**(-exponent)
            
            # ----- Return the acceleration
            
            return v.scale(a/d)
        
        return gen
    
    # ----------------------------------------------------------------------------------------------------
    # Attraction from a location
    
    @staticmethod
    def func_attraction(location=(0, 0, 0), intensity=10, exponent=-2, d_min=.2):
        """ Returns a function which builds an attraction acceleration towards the given location.
        
        The attraction can be used to simulate Newton gravity law with ``` exponent = -2```.
        
        The acceleration is computed with ``` a = intensity / distance**exponent ```
        
        To avoid infinite accelerations, the distance is minimized with d_min.
        
        Note that if the intensity is negative, the attractor becomes a repulsor!
        
        The function returned by this method can be used as an argument in a simulation zone creation method:
        
        ``` python    
        simul = gn.Simulation.Fluid(acceleration=gn.Simulation.func_attraction(...))    
        ```
        
        or, if more than one acceleration function is required
        
        ``` python
        simul = gn.Simulation.Fluid(acceleration={
            'gravity'    : gn.Simulation.func_gravity(),
            'attraction' : gn.Simulation.func_attraction(...),
            })
        ```
        
        Args:
            - location (Vector) : location of the attractor
            - intensity (Float) : intensity of the attraction
            - exponent (Float) : exponent parameter of the acceleration
            - d_min (Float) : minimum distance to avoid infinite accelerations
        
        Returns:
            - function(**kwargs) : nodes generator
        """    
        
        import geonodes as gn
    
        def gen(simul):
            
            cloud = simul.cloud
            
            # ----- Vector to the attractor location
            
            v = location - cloud.points.position
            
            # ----- Minimum distance to the attractor
            
            d = v.length
            l = d.switch(d.less_than(d_min), d_min)
            
            # ----- Acceleration norm
            
            a = intensity*l**exponent
            
            # ----- Return the acceleration
            
            return v.scale(a/d)
        
        return gen
    
    # ====================================================================================================
    # Surface interaction
    
    # ----------------------------------------------------------------------------------------------------
    # Stick the particle on to the surface
    
    @staticmethod
    def func_stick_on_surface(mesh, kill_outside=False, z_max=50):
        """ Returns a function building nodes which place the particles on the surface.
        
        The algorithm using the raycats node to project the particles onto the surface, ```z_max``` is the latitude from which to project the particles.
        
        if particles are outside the surface, they can be deleted if kiil_outside is True.
        
        The function returned by this method can be used as an argument in a simulation zone creation method:
        
        ``` python    
        simul = gn.Simulation.Fluid(finish=gn.Simulation.func_stick_on_surface(...))    
        ```
        
        or, if more than one finish function is required
        
        ``` python
        simul = gn.Simulation.Fluid(finish={
            'stick' : gn.Simulation.func_stick_on_surface(...),
            })
        ```
        
        Args:
            - mesh (Mesh) : the surface
            - kill_outside (bool) : delete or not the particles outside the surface
            - z_max (float) : the altitude higher that the surface to raycast from
        
        Returns:
            - function(**kwargs) : nodes generator
        """
        
        import geonodes as gn
        
        def gen(simul):
            
            cloud = simul.cloud
            
            # ----- Location to raycast from
            
            loc = cloud.points.position
            loc.z = z_max
            
            # ------ Raycast to the surface from the points locations
            
            node = cloud.points.raycast(target_geometry=mesh, source_position=loc, ray_length=2*z_max)
            
            # ----- Locate the where we have a hit
            
            cloud.points[node.is_hit].position = node.hit_position
            
            # ----- Delete the particles outside the surface
            
            if kill_outside:
                cloud.points[node.is_hit.b_not()].delete()
            
        return gen
    
    # ----------------------------------------------------------------------------------------------------
    # Acceleration along the slope
    
    @staticmethod
    def func_surface_flow(mesh, gravity=(0, 0, -10)):
        """ Returns a function which builds an acceleration following the surface slope.
        
        The function returned by this method can be used as an argument in a simulation zone creation method:
        
        ``` python    
        simul = gn.Simulation.Fluid(acceleration=gn.Simulation.func_surface_flow(...))    
        ```
        
        or, if more than one acceleration function is required
        
        ``` python
        simul = gn.Simulation.Fluid(acceleration={
            'viscosity'  : gn.Simulation.func_viscosity(),
            'flow'       : gn.Simulation.func_surface_flow(...),
            })
        ```
        
        Args:
            - mesh (Mesh)       : the surface
            - gravity (Vector)  : gravity vector
            - intensity (Float) : intensity of the attraction
            - exponent (Float) : exponent parameter of the acceleration
            - d_min (Float) : minimum distance to avoid infinite accelerations
        
        Returns:
            - function(**kwargs) : nodes generator
        """       
        
        import geonodes as gn
        
        g = gn.Vector(gravity)
        
        def gen(simul):
            
            cloud = simul.cloud
            
            # ----- Get the normal at each point
            
            normal = mesh.sample_nearest_surface(value=mesh.verts.normal, sample_position=cloud.points.position)
            
            # ----- Gravity component
            
            return normal.cross(g).cross(normal)
        
        return gen
    
    # ----------------------------------------------------------------------------------------------------
    # Bounce on the surface of an object
    
    @staticmethod
    def func_bounce(mesh, distance=.1, damp=0.):
        """ Returns a function creating a bounce simulation onto a mesh.
        
        The created nodes test if the points are below the closest surface. If it is the case,
        it places the points on the external side of the face an reflect the speed with the normal to thge surface.
        
        The function returned by this method can be used as the setpt argument in a simulation zone creation method:
        
        ``` python    
        simul = gn.Simulation.Fluid(setup=gn.Simulation.func_bounce(...))    

        
        Args:
            - mesh (Mesh)       : the surface
            - distance (float)  : distance from the surface
            - damp (float)      : damp factor 
        
        Returns:
            - function(**kwargs) : nodes generator
        """       
    
        import geonodes as gn
    
        def gen(simul):
            
            cloud = simul.cloud
            
            velocity = cloud.points.named_vector("velocity")
            
            prox_node = cloud.points.proximity(target=mesh, source_position=cloud.points.position)
            v = prox_node.position - cloud.points.position
            
            rc_node = cloud.points.raycast(
                target_geometry  = mesh, 
                source_position  = cloud.points.position,
                ray_direction    = v,
                ray_length       = 5*distance)
                
            sel = rc_node.is_hit * rc_node.hit_normal.dot(velocity).less_than(0)
            
            cloud.points.store_named_attribute("temp_sel", sel)
            sel = cloud.points.named_boolean("temp_sel")
            
            cloud.points[sel].position = rc_node.hit_position + rc_node.hit_normal.scale(distance)
            
            if True:
                cloud.points[sel].store_named_attribute("velocity", velocity.reflect(rc_node.hit_normal).scale(1-damp))
                simul.cloud = cloud
            else:
                new_vel = velocity.switch(sel, velocity.reflect(rc_node.hit_normal).scale(1-damp))
                cloud.points.store_named_attribute("velocity", new_vel)
            
        return gen 
        
    # ----------------------------------------------------------------------------------------------------
    # Generation function calling a group
    
    @staticmethod
    def func_group(group_name, in_delta_time=None, in_cloud=None, out_cloud=None, out_socket=None):
        """ Returns a function creating a Group node of the given name and connect sockets.
        
        The Group can have input sockets for delta_time and cloud used in a fluid simulation.
        It can have an output sockets for cloud if the cloud has been changed.
        
        An additional output socket can be specified if the node must return a value such as an acceleration.
        
        If the sockets exist with this name, they will be connected automatically. If they have differente names,
        they must be provided using in_... and out_... arguments, for instance:
        - ``` in_cloud = None ``` : the cloud will be plugged to the input socket named 'cloud', 'points' or 'geometry' if it exists
        - ``` out_cloud = 'geometry' ``` : the cloud will be plugged to the input socket named 'vector'
        
        The same is done for the output socket: variables are updated to match to the corresponding outpout sockets.
        
        If the out_socket argument is not node, the generated function return the correspondint outpout socket of the group node.
        
        The function returned by this method can be used as an argument in a simulation zone creation method:
        
        ``` python    
        simul = gn.Simulation.Fluid(acceleration=gn.Simulation.func_group("Custom Acceleration", out_socket='acceleration())    
        ```
        
        Args:
            - group_name (string) : the name of the Group node
            - out_socket (str=None) : name of the output socket of the created group node to return
            - in_delta_time (str=None) : nema of the *delta time* input socket
            - in_cloud (str=None) : nema of the *cloud* input socket
            - in_velocity (str=None) : nema of the *velocity* input socket
            - in_age (str=None) : nema of the *age* input socket
            - out_cloud (str=None) : nema of the *cloud* output socket
            - out_velocity (str=None) : nema of the *velocity* output socket
            - out_age (str=None) : nema of the *age* output socket
        
        Returns:
            - function(**kwargs) : nodes generator
        """
        
        import geonodes as gn
        
        def gen(simul):
            
            cloud = simul.cloud
            
            # ----- Generate the group
            
            node = gn.Group(group_name)
            
            # ----- Input socket names
            
            in_d = in_delta_time
            in_c = in_cloud
            
            if in_d is None:
                if 'delta_time' in node.insockets.keys():
                    in_d = 'delta_time'
            if in_c is None:
                if 'cloud' in node.insockets.keys():
                    in_c = 'cloud'
                elif 'points' in node.insockets.keys():
                    in_c = 'points'
                elif 'geometry' in node.insockets.keys():
                    in_c = 'geometry'
    
            # ----- Connect the input sockets
    
            if in_d is not None:
                setattr(node, in_d, simul.delta_time)
            if in_c is not None:
                setattr(node, in_c, cloud)
    
            # ----- Output socket names
            
            out_c = out_cloud
            
            if out_c is None:
                if 'cloud' in node.outsockets.keys():
                    out_c = 'cloud'
                elif 'points' in node.outsockets.keys():
                    out_c = 'points'
                elif 'geometry' in node.outsockets.keys():
                    out_c = 'geometry'

            # ----- Connect the output sockets
            # Make the data sockets pointing to the outpout sockets of the node
            # using the stack method        
                    
            if out_c is not None:
                cloud.stack(node, out_c)
                
            simul.cloud = cloud
                
            # ----- Return the output socket if a name is given
                
            if out_socket is not None:
                return getattr(node, out_socket)
            else:
                return None
                
        return gen
         
        
            
            
                
        
    
            
        
        
        
        