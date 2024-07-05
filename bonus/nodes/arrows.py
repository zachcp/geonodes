#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Jul  5 2024

@author: alain

-----------------------------------------------------
geonodes module
- Generates nodes with python
- Use numpy to manage vertices
-----------------------------------------------------

module : arrows
---------------

Generates Geometry Nodes to generate arrows. Arrows have the exact size. They can be generated
from points to generate a field of vectors.
They can also be generated individually, either from cartesian, cylindrical or spherical coordinates.


The field of arrows make use of 'Vectors' named attribute
Parameters for shader are passed through attributes:
    - Color
    - Transparency
    - Negative

Default material name is Arrow with is generated by this module

Shaders
-------
    - Arrow

Geometry Nodes
--------------
    - Arrows : a field of vectors
    - Arrow  : a single vector definef by cartesian components
    - Polar Arrow : a single vector defined by cylindrical components
    - Spherical Arrow : a single vector defined by cylindrical components
    - To Lines of Field : transform curve to lines
"""

import bpy
import geonodes as gn


def build_arrows(create_shaders=False):

    print("\nCreate Arrows shaders and nodes...")

    # ====================================================================================================
    # Default Shader for Arrow

    if not gn.Shader.tree_exists("Arrow") or create_shaders:
        with gn.Shader("Arrow") as tree:

            pos_color = tree.Attribute(attribute_type='GEOMETRY', attribute_name="Color").vector
            negative  = tree.Attribute(attribute_type='GEOMETRY', attribute_name="Negative").fac
            transp    = tree.Attribute(attribute_type='GEOMETRY', attribute_name="Transparency").fac

            neg_color = tree.HueSaturationValue(color=pos_color, hue=.5, saturation=.9, value=.9).color
            color = pos_color.mix(negative, neg_color)

            ped = tree.PrincipledBSDF(
                base_color = color,
                roughness  = negative.map_range(to_min=.1, to_max=.9),
            ).bsdf

            shader = tree.MixShader(fac=transp, shader=ped, shader_1=tree.TransparentBSDF().bsdf)

            tree.surface = shader

    # ====================================================================================================
    # Geometry Nodes

    # ----------------------------------------------------------------------------------------------------
    # Arrows field

    with gn.GeoNodes("Arrows", fake_user=True) as tree:

        points     = tree.geometry

        scale      = tree.float_input(       "Scale",        1.,  min_value=0., description = "Vectors multiplicator")
        resol      = tree.int_input(         "Resolution",   12,  min_value=3, max_value=64, description = "Arrows shaft resolution")
        section    = tree.float_input(       "Section",      .02, min_value=0., max_value=1., description = "Arrows shaft radius")
        use_sphere = tree.bool_input(        "Sphere",       False, description="Use a sphere for the head rather than a cone")
        color      = tree.color_input(       "Color",        (0., 0., 1., 1.), description="Color to pass as 'Color' named attribute for shader")
        transp     = tree.float_input(       "Transparency", 0., description="Transparency factor to pass as 'Transparency' named attribute for shader")
        negative   = tree.factor_input(      "Negative",     0., min_value=0., max_value=1., description="Negative factor to pass as 'Negative', named attribute for shader")
        shaft_mat  = tree.material_input(    "Shaft",        "Arrow", description="Material for the shaft")
        head_mat   = tree.material_input(    "Head",         "Arrow", description="Material for the head")
        show_arrow = tree.bool_input(        "Show",         True, description="Show / hide flag")

        vectors = points.POINT.named_vector("Vectors")

        with tree.layout("Length and rotation"):
            length = vectors.length()*scale
            rot    = tree.AlignEulerToVector(axis='Z', vector=vectors).rotation

        with tree.layout("Arrow Heads"):

            with tree.layout("Cone"):
                cone_height = section*7
                cone = tree.Cone(vertices=2*resol, radius_bottom=section*3., depth=cone_height).mesh

            with tree.layout("Sphere"):
                radius = section*4
                sphere_height = radius
                sphere = tree.UVSphere(segments=2*resol, rings=resol, radius=radius).mesh
                #sphere.transform_geometry(translation=(0, 0, radius))

            head = cone.switch(use_sphere, sphere)
            head_height = cone_height.switch(use_sphere, sphere_height)
            ratio = length/(length + head_height)
            head.set_material(head_mat)

            with tree.layout("Instanciate heads"):
                heads = points.instance_on_points(instance=head, scale=(1, 1, ratio))
                heads.rotate_instances(rotation=rot)
                heads.translate_instances(translation=vectors.scale((length*ratio)/vectors.length()), local_space=False)

        with tree.layout("Arrow shafts"):
            shaft = tree.Cylinder(vertices=resol, radius=section, depth=1.).mesh
            shaft.transform_geometry(translation=(0, 0, .5))
            shaft.set_material(shaft_mat)
            shafts = points.instance_on_points(instance=shaft, scale=(1, 1, length*ratio))
            shafts.rotate_instances(rotation=rot)

        with tree.layout("Finalize"):

            shafts.INSTANCE[length.equal(0)].delete_geometry()
            heads.INSTANCE[length.equal(0)].delete_geometry()

            arrows = (shafts + heads).realize_instances()
            arrows.FACE.set_shade_smooth()

            arrows.POINT.store_named_vector("Color",  color)
            arrows.POINT.store_named_float( "Transparency", transp)
            arrows.POINT.store_named_float( "Negative",     negative)


        tree.geometry = arrows.switch(-show_arrow)


    # ----------------------------------------------------------------------------------------------------
    # Single Arrow defined by its cartesian components

    with gn.GeoNodes("Arrow", fake_user=True) as tree:

        location   = tree.vector_input(      "Location", description="Vector location")
        vector     = tree.vector_input(      "Vector",       (1, 0, 0), description="Vector components")

        scale      = tree.float_input(       "Scale",        1.,  min_value=0., description = "Vector multiplicator")
        resol      = tree.int_input(         "Resolution",   12,  min_value=3, max_value=64, description = "Arrow shaft resolution")
        section    = tree.float_input(       "Section",      .02, min_value=0., max_value=1., description = "Arrow shaft radius")
        use_sphere = tree.bool_input(        "Sphere",       False, description="Use a sphere for the head rather than a cone")
        color      = tree.color_input(       "Color",        (0., 0., 1., 1.), description="Color to pass as 'Color' named attribute for shader")
        transp     = tree.float_input(       "Transparency", 0., description="Transparency factor to pass as 'Transparency' named attribute for shader")
        negative   = tree.factor_input(      "Negative",     0., min_value=0., max_value=1., description="Negative factor to pass as 'Negative', named attribute for shader")
        shaft_mat  = tree.material_input(    "Shaft",        "Arrow", description="Material for the shaft")
        head_mat   = tree.material_input(    "Head",         "Arrow", description="Material for the head")
        show_arrow = tree.bool_input(        "Show",         True, description="Show +/ hide flag")

        points = tree.Points(count=1, position=location).points
        points.POINT.store_named_vector("Vectors", vector)

        tree.geometry = tree.group("Arrows", points,
            scale        = scale,
            resolution   = resol,
            section      = section,
            sphere       = use_sphere,
            color        = color,
            transparency = transp,
            negative     = negative,
            shaft        = shaft_mat,
            head         = head_mat,
            show         = show_arrow,
            ).geometry

    # ----------------------------------------------------------------------------------------------------
    # Single arrow defined by cylindrical components

    with gn.GeoNodes("Polar Arrow", fake_user=True) as tree:

        location   = tree.vector_input(      "Location", description="Vector location")
        length     = tree.float_input(       "Length",   1., min_value=0, description="Vector length")
        angle      = tree.angle_input(       "Angle",    0., description="Polar angle in plane XY")
        z          = tree.float_input(       "z",        0., description="z component")

        scale      = tree.float_input(       "Scale",        1.,  min_value=0., description = "Vector multiplicator")
        resol      = tree.int_input(         "Resolution",   12,  min_value=3, max_value=64, description = "Arrow shaft resolution")
        section    = tree.float_input(       "Section",      .02, min_value=0., max_value=1., description = "Arrow shaft radius")
        use_sphere = tree.bool_input(        "Sphere",       False, description="Use a sphere for the head rather than a cone")
        color      = tree.color_input(       "Color",        (0., 0., 1., 1.), description="Color to pass as 'Color' named attribute for shader")
        transp     = tree.float_input(       "Transparency", 0., description="Transparency factor to pass as 'Transparency' named attribute for shader")
        negative   = tree.factor_input(      "Negative",     0., min_value=0., max_value=1., description="Negative factor to pass as 'Negative', named attribute for shader")
        shaft_mat  = tree.material_input(    "Shaft",        "Arrow", description="Material for the shaft")
        head_mat   = tree.material_input(    "Head",         "Arrow", description="Material for the head")
        show_arrow = tree.bool_input(        "Show",         True, description="Show +/ hide flag")

        vector = tree.vector((length*tree.cos(angle), length*tree.sin(angle), z))

        points = tree.Points(count=1, position=location).points
        points.POINT.store_named_vector("Vectors", vector)

        tree.geometry = tree.group("Arrows", points,
            scale        = scale,
            resolution   = resol,
            section      = section,
            sphere       = use_sphere,
            color        = color,
            transparency = transp,
            negative     = negative,
            shaft        = shaft_mat,
            head         = head_mat,
            show         = show_arrow,
            ).geometry

    # ----------------------------------------------------------------------------------------------------
    # Single arrow defined by its spherical components

    with gn.GeoNodes("Spherical Arrow", fake_user=True) as tree:

        location   = tree.vector_input(      "Location",  description="Vector location")
        length     = tree.float_input(       "Length",    1., min_value=0, description="Vector length")
        theta      = tree.angle_input(       "Longitude", 0., description="Longitude : angle in XY plane")
        phi        = tree.float_input(       "Latitude",  0., description="Latitude : angle from XY plane to Z axis")

        scale      = tree.float_input(       "Scale",        1.,  min_value=0., description = "Vector multiplicator")
        resol      = tree.int_input(         "Resolution",   12,  min_value=3, max_value=64, description = "Arrow shaft resolution")
        section    = tree.float_input(       "Section",      .02, min_value=0., max_value=1., description = "Arrow shaft radius")
        use_sphere = tree.bool_input(        "Sphere",       False, description="Use a sphere for the head rather than a cone")
        color      = tree.color_input(       "Color",        (0., 0., 1., 1.), description="Color to pass as 'Color' named attribute for shader")
        transp     = tree.float_input(       "Transparency", 0., description="Transparency factor to pass as 'Transparency' named attribute for shader")
        negative   = tree.factor_input(      "Negative",     0., min_value=0., max_value=1., description="Negative factor to pass as 'Negative', named attribute for shader")
        shaft_mat  = tree.material_input(    "Shaft",        "Arrow", description="Material for the shaft")
        head_mat   = tree.material_input(    "Head",         "Arrow", description="Material for the head")
        show_arrow = tree.bool_input(        "Show",         True, description="Show +/ hide flag")

        cos_phi = tree.cos(phi)
        vector = length*tree.vector((cos_phi*tree.cos(angle), cos_phi*tree.sin(angle), tree.sin(phi)))

        points = tree.Points(count=1, position=location).points
        points.POINT.store_named_vector("Vectors", vector)

        tree.geometry = tree.group("Arrows", points,
            scale        = scale,
            resolution   = resol,
            section      = section,
            sphere       = use_sphere,
            color        = color,
            transparency = transp,
            negative     = negative,
            shaft        = shaft_mat,
            head         = head_mat,
            show         = show_arrow,
            ).geometry

    # ====================================================================================================
    # Lines

    with gn.GeoNodes("To Lines of Field", fake_user=True) as tree:

        resol   = tree.int_input(       "Resolution",       12, min_value=3, max_value=64, description="Lines geometry resolution")
        radius  = tree.float_input(     "Radius",           .02, min_value=0., max_value=1., description="Lines radius")
        int_fac = tree.factor_input(    "Intensity factor", 0., min_value=0., max_value=1., description="Radius proportional to 'Intensity' named attribute")

        transp = tree.factor_input(     "Transparency",     0., min_value=0., max_value=1., description="Transparency factor to pass as 'Transparency' named attribute for shader")
        color  = tree.color_input(      "Color",            (.7, .2, .2, 1.), description = "Color to pass as 'Color' named attribute for shader")
        mat    = tree.material_input(   "Material", description="Lines material")
        show   = tree.bool_input(       "Show",             True, description="Show / Hide flag")

        # ----------------------------------------------------------------------------------------------------
        # Main

        with tree.layout("Curves"):
            comps_node = tree.geometry.separate_components()
            curves = comps_node.curve + comps_node.mesh.mesh_to_curve()

        curves.store_named_vector("Color", color)
        curves.store_named_float("Transparency", transp)

        with tree.layout("Intensity"):
            int_base = curves.named_float("Intensity")
            stats = curves.POINT.attribute_statistic(attribute=int_base)
            intensity = int_base.map_range(stats.min, stats.max, int_fac.map_range(to_min=1., to_max=.01), 1., interpolation_type='SMOOTHERSTEP')
            curves.radius = intensity

        mesh = curves.curve_to_mesh(profile_curve=tree.CurveCircle(radius=radius, resolution=resol).curve)

        mesh.FACE.material     = mat
        mesh.FACE.shade_smooth = True

        # ----- Done

        tree.geometry = mesh.switch(-show)
