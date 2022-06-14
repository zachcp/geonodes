#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2022-06-14
@author: Generated from generator module
Blender version: 3.2.0
"""

import geonodes as gn
from geonodes.core import datasockets as dsock
from geonodes.nodes import nodes
import logging
logger = logging.Logger('geonodes')

# ==============================================================================================================
# Data class Spline

class Spline(gn.Geometry):
    """ 

    Data socket Spline
    ------------------
        > Inherits from gn.Geometry
          
        <sub>go to index</sub>
        
        
    

        Attribute capture
        -----------------
            - capture_cyclic : cyclic (Boolean)
            - capture_endpoint_selection : selection (Boolean)
            - capture_handle_positions : Sockets      [left (Vector), right (Vector)]
            - capture_handle_type_selection : selection (Boolean)
            - capture_length : Sockets      [length (Float), point_count (Integer)]
            - capture_parameter : Sockets      [factor (Float), length (Float), index (Integer)]
            - capture_resolution : resolution (Integer)
            - capture_tangent : tangent (Vector)
            - capture_tilt : tilt (Float)
    

        Attributes
        ----------
            - cyclic : Boolean = capture_cyclic(domain='CURVE')
            - endpoint_selection : Boolean = capture_endpoint_selection(domain='CURVE')
            - factor : Float = capture_parameter(domain='CURVE').factor
            - handle_type_selection : Boolean = capture_handle_type_selection(domain='CURVE')
            - left_handle_position : Vector = capture_handle_positions(domain='CURVE').left
            - length : Float = capture_length(domain='CURVE').length
            - parameter_index : Integer = capture_parameter(domain='CURVE').index
            - parameter_length : Float = capture_parameter(domain='CURVE').length
            - point_count : Integer = capture_length(domain='CURVE').point_count
            - resolution : Integer = capture_resolution(domain='CURVE')
            - right_handle_position : Vector = capture_handle_positions(domain='CURVE').right
            - spline_ID : Integer = capture_ID(domain='SPLINE')
            - spline_index : Integer = capture_index(domain='SPLINE')
            - spline_position : Integer = capture_position(domain='SPLINE')
            - tangent : Vector = capture_tangent(domain='CURVE')
            - tilt : Float = capture_tilt(domain='CURVE')
    

        Methods
        -------
            - duplicate_splines : Sockets      [geometry (Geometry), duplicate_index (Integer)]
            - set_cyclic : geometry (Geometry)
            - set_resolution : geometry (Geometry)
    """


    # ----------------------------------------------------------------------------------------------------
    # Attribute capture

    def capture_handle_positions(self, relative=None, domain='CURVE', node_label = None, node_color = None):
        """ > Node: CurveHandlePositions
          
        <sub>go to: top index
        blender ref GeometryNodeInputCurveHandlePositions
        node ref Curve Handle Positions </sub>
                                  
        ```python
        v = spline.capture_handle_positions(self, relative, domain='CURVE', node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - relative : Boolean## Parameters
            - self
            - domain:'CURVE'
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.CurveHandlePositions(relative=relative, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [left (Vector), right (Vector)]
            
        """

        attr_name = 'capture_handle_positions_' + domain
        node = self.attr_props.get(attr_name)
        if node is None:
            node = nodes.CurveHandlePositions(relative=relative, label=node_label, node_color=node_color)
            node.as_attribute(owning_socket=self, domain=domain)
            self.attr_props[attr_name] = node
        return node

    def capture_tangent(self, domain='CURVE', node_label = None, node_color = None):
        """ > Node: CurveTangent
          
        <sub>go to: top index
        blender ref GeometryNodeInputTangent
        node ref Curve Tangent </sub>
                                  
        ```python
        v = spline.capture_tangent(self, domain='CURVE', node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
            - domain:'CURVE'
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.CurveTangent(label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Vector
            
        """

        attr_name = 'capture_tangent_' + domain
        node = self.attr_props.get(attr_name)
        if node is None:
            node = nodes.CurveTangent(label=node_label, node_color=node_color)
            node.as_attribute(owning_socket=self, domain=domain)
            self.attr_props[attr_name] = node
        return node.tangent

    def capture_tilt(self, domain='CURVE', node_label = None, node_color = None):
        """ > Node: CurveTilt
          
        <sub>go to: top index
        blender ref GeometryNodeInputCurveTilt
        node ref Curve Tilt </sub>
                                  
        ```python
        v = spline.capture_tilt(self, domain='CURVE', node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
            - domain:'CURVE'
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.CurveTilt(label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Float
            
        """

        attr_name = 'capture_tilt_' + domain
        node = self.attr_props.get(attr_name)
        if node is None:
            node = nodes.CurveTilt(label=node_label, node_color=node_color)
            node.as_attribute(owning_socket=self, domain=domain)
            self.attr_props[attr_name] = node
        return node.tilt

    def capture_endpoint_selection(self, start_size=None, end_size=None, domain='CURVE', node_label = None, node_color = None):
        """ > Node: EndpointSelection
          
        <sub>go to: top index
        blender ref GeometryNodeCurveEndpointSelection
        node ref Endpoint Selection </sub>
                                  
        ```python
        v = spline.capture_endpoint_selection(self, start_size, end_size, domain='CURVE', node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - start_size : Integer
            - end_size : Integer## Parameters
            - self
            - domain:'CURVE'
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.EndpointSelection(start_size=start_size, end_size=end_size, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        attr_name = 'capture_endpoint_selection_' + domain
        node = self.attr_props.get(attr_name)
        if node is None:
            node = nodes.EndpointSelection(start_size=start_size, end_size=end_size, label=node_label, node_color=node_color)
            node.as_attribute(owning_socket=self, domain=domain)
            self.attr_props[attr_name] = node
        return node.selection

    def capture_handle_type_selection(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}, domain='CURVE', node_label = None, node_color = None):
        """ > Node: HandleTypeSelection
          
        <sub>go to: top index
        blender ref GeometryNodeCurveHandleTypeSelection
        node ref Handle Type Selection </sub>
                                  
        ```python
        v = spline.capture_handle_type_selection(self, handle_type, mode, domain='CURVE', node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
            - handle_type : 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
            - mode : {'RIGHT', 'LEFT'}
            - domain:'CURVE'
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.HandleTypeSelection(handle_type=handle_type, mode=mode, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        attr_name = 'capture_handle_type_selection_' + domain
        node = self.attr_props.get(attr_name)
        if node is None:
            node = nodes.HandleTypeSelection(handle_type=handle_type, mode=mode, label=node_label, node_color=node_color)
            node.as_attribute(owning_socket=self, domain=domain)
            self.attr_props[attr_name] = node
        return node.selection

    def capture_cyclic(self, domain='CURVE', node_label = None, node_color = None):
        """ > Node: IsSplineCyclic
          
        <sub>go to: top index
        blender ref GeometryNodeInputSplineCyclic
        node ref Is Spline Cyclic </sub>
                                  
        ```python
        v = spline.capture_cyclic(self, domain='CURVE', node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
            - domain:'CURVE'
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.IsSplineCyclic(label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Boolean
            
        """

        attr_name = 'capture_cyclic_' + domain
        node = self.attr_props.get(attr_name)
        if node is None:
            node = nodes.IsSplineCyclic(label=node_label, node_color=node_color)
            node.as_attribute(owning_socket=self, domain=domain)
            self.attr_props[attr_name] = node
        return node.cyclic

    def capture_length(self, domain='CURVE', node_label = None, node_color = None):
        """ > Node: SplineLength
          
        <sub>go to: top index
        blender ref GeometryNodeSplineLength
        node ref Spline Length </sub>
                                  
        ```python
        v = spline.capture_length(self, domain='CURVE', node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
            - domain:'CURVE'
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SplineLength(label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [length (Float), point_count (Integer)]
            
        """

        attr_name = 'capture_length_' + domain
        node = self.attr_props.get(attr_name)
        if node is None:
            node = nodes.SplineLength(label=node_label, node_color=node_color)
            node.as_attribute(owning_socket=self, domain=domain)
            self.attr_props[attr_name] = node
        return node

    def capture_parameter(self, domain='CURVE', node_label = None, node_color = None):
        """ > Node: SplineParameter
          
        <sub>go to: top index
        blender ref GeometryNodeSplineParameter
        node ref Spline Parameter </sub>
                                  
        ```python
        v = spline.capture_parameter(self, domain='CURVE', node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
            - domain:'CURVE'
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SplineParameter(label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [factor (Float), length (Float), index (Integer)]
            
        """

        attr_name = 'capture_parameter_' + domain
        node = self.attr_props.get(attr_name)
        if node is None:
            node = nodes.SplineParameter(label=node_label, node_color=node_color)
            node.as_attribute(owning_socket=self, domain=domain)
            self.attr_props[attr_name] = node
        return node

    def capture_resolution(self, domain='CURVE', node_label = None, node_color = None):
        """ > Node: SplineResolution
          
        <sub>go to: top index
        blender ref GeometryNodeInputSplineResolution
        node ref Spline Resolution </sub>
                                  
        ```python
        v = spline.capture_resolution(self, domain='CURVE', node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
            - domain:'CURVE'
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SplineResolution(label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Integer
            
        """

        attr_name = 'capture_resolution_' + domain
        node = self.attr_props.get(attr_name)
        if node is None:
            node = nodes.SplineResolution(label=node_label, node_color=node_color)
            node.as_attribute(owning_socket=self, domain=domain)
            self.attr_props[attr_name] = node
        return node.resolution


    # ----------------------------------------------------------------------------------------------------
    # Attributes

    @property
    def spline_ID(self):
        """ > Node: ID
          
        <sub>go to: top index
        blender ref GeometryNodeInputID
        node ref ID </sub>
                                  
        ```python
        v = spline.spline_ID(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.ID()
            ```
    

        Returns
        -------
            Integer
            
        """

        return self.capture_ID(domain='SPLINE')

    @property
    def spline_index(self):
        """ > Node: Index
          
        <sub>go to: top index
        blender ref GeometryNodeInputIndex
        node ref Index </sub>
                                  
        ```python
        v = spline.spline_index(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Index()
            ```
    

        Returns
        -------
            Integer
            
        """

        return self.capture_index(domain='SPLINE')

    @property
    def spline_position(self):
        """ > Node: Index
          
        <sub>go to: top index
        blender ref GeometryNodeInputIndex
        node ref Index </sub>
                                  
        ```python
        v = spline.spline_position(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.Index()
            ```
    

        Returns
        -------
            Integer
            
        """

        return self.capture_position(domain='SPLINE')

    @property
    def left_handle_position(self, relative=None):
        """ > Node: CurveHandlePositions
          
        <sub>go to: top index
        blender ref GeometryNodeInputCurveHandlePositions
        node ref Curve Handle Positions </sub>
                                  
        ```python
        v = spline.left_handle_position(self, relative)
        ```
    

        Arguments
        ---------
            ## Sockets
            - relative : Boolean## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.CurveHandlePositions(relative=relative)
            ```
    

        Returns
        -------
            Vector
            
        """

        return self.capture_handle_positions(domain='CURVE').left

    @property
    def right_handle_position(self, relative=None):
        """ > Node: CurveHandlePositions
          
        <sub>go to: top index
        blender ref GeometryNodeInputCurveHandlePositions
        node ref Curve Handle Positions </sub>
                                  
        ```python
        v = spline.right_handle_position(self, relative)
        ```
    

        Arguments
        ---------
            ## Sockets
            - relative : Boolean## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.CurveHandlePositions(relative=relative)
            ```
    

        Returns
        -------
            Vector
            
        """

        return self.capture_handle_positions(domain='CURVE').right

    @property
    def tangent(self):
        """ > Node: CurveTangent
          
        <sub>go to: top index
        blender ref GeometryNodeInputTangent
        node ref Curve Tangent </sub>
                                  
        ```python
        v = spline.tangent(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.CurveTangent()
            ```
    

        Returns
        -------
            Vector
            
        """

        return self.capture_tangent(domain='CURVE')

    @property
    def tilt(self):
        """ > Node: CurveTilt
          
        <sub>go to: top index
        blender ref GeometryNodeInputCurveTilt
        node ref Curve Tilt </sub>
                                  
        ```python
        v = spline.tilt(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.CurveTilt()
            ```
    

        Returns
        -------
            Float
            
        """

        return self.capture_tilt(domain='CURVE')

    @property
    def endpoint_selection(self, start_size=None, end_size=None):
        """ > Node: EndpointSelection
          
        <sub>go to: top index
        blender ref GeometryNodeCurveEndpointSelection
        node ref Endpoint Selection </sub>
                                  
        ```python
        v = spline.endpoint_selection(self, start_size, end_size)
        ```
    

        Arguments
        ---------
            ## Sockets
            - start_size : Integer
            - end_size : Integer## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.EndpointSelection(start_size=start_size, end_size=end_size)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return self.capture_endpoint_selection(domain='CURVE')

    @property
    def handle_type_selection(self, handle_type='AUTO', mode={'RIGHT', 'LEFT'}):
        """ > Node: HandleTypeSelection
          
        <sub>go to: top index
        blender ref GeometryNodeCurveHandleTypeSelection
        node ref Handle Type Selection </sub>
                                  
        ```python
        v = spline.handle_type_selection(self, handle_type, mode)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
            - handle_type : 'AUTO' in [FREE, AUTO, VECTOR, ALIGN]
            - mode : {'RIGHT', 'LEFT'}
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.HandleTypeSelection(handle_type=handle_type, mode=mode)
            ```
    

        Returns
        -------
            Boolean
            
        """

        return self.capture_handle_type_selection(domain='CURVE')

    @property
    def cyclic(self):
        """ > Node: IsSplineCyclic
          
        <sub>go to: top index
        blender ref GeometryNodeInputSplineCyclic
        node ref Is Spline Cyclic </sub>
                                  
        ```python
        v = spline.cyclic(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.IsSplineCyclic()
            ```
    

        Returns
        -------
            Boolean
            
        """

        return self.capture_cyclic(domain='CURVE')

    @property
    def length(self):
        """ > Node: SplineLength
          
        <sub>go to: top index
        blender ref GeometryNodeSplineLength
        node ref Spline Length </sub>
                                  
        ```python
        v = spline.length(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SplineLength()
            ```
    

        Returns
        -------
            Float
            
        """

        return self.capture_length(domain='CURVE').length

    @property
    def point_count(self):
        """ > Node: SplineLength
          
        <sub>go to: top index
        blender ref GeometryNodeSplineLength
        node ref Spline Length </sub>
                                  
        ```python
        v = spline.point_count(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SplineLength()
            ```
    

        Returns
        -------
            Integer
            
        """

        return self.capture_length(domain='CURVE').point_count

    @property
    def factor(self):
        """ > Node: SplineParameter
          
        <sub>go to: top index
        blender ref GeometryNodeSplineParameter
        node ref Spline Parameter </sub>
                                  
        ```python
        v = spline.factor(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SplineParameter()
            ```
    

        Returns
        -------
            Float
            
        """

        return self.capture_parameter(domain='CURVE').factor

    @property
    def parameter_length(self):
        """ > Node: SplineParameter
          
        <sub>go to: top index
        blender ref GeometryNodeSplineParameter
        node ref Spline Parameter </sub>
                                  
        ```python
        v = spline.parameter_length(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SplineParameter()
            ```
    

        Returns
        -------
            Float
            
        """

        return self.capture_parameter(domain='CURVE').length

    @property
    def parameter_index(self):
        """ > Node: SplineParameter
          
        <sub>go to: top index
        blender ref GeometryNodeSplineParameter
        node ref Spline Parameter </sub>
                                  
        ```python
        v = spline.parameter_index(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SplineParameter()
            ```
    

        Returns
        -------
            Integer
            
        """

        return self.capture_parameter(domain='CURVE').index

    @property
    def resolution(self):
        """ > Node: SplineResolution
          
        <sub>go to: top index
        blender ref GeometryNodeInputSplineResolution
        node ref Spline Resolution </sub>
                                  
        ```python
        v = spline.resolution(self)
        ```
    

        Arguments
        ---------
            ## Parameters
            - self
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SplineResolution()
            ```
    

        Returns
        -------
            Integer
            
        """

        return self.capture_resolution(domain='CURVE')


    # ----------------------------------------------------------------------------------------------------
    # Methods

    def set_cyclic(self, selection=None, cyclic=None, node_label = None, node_color = None):
        """ > Node: SetSplineCyclic
          
        <sub>go to: top index
        blender ref GeometryNodeSetSplineCyclic
        node ref Set Spline Cyclic </sub>
                                  
        ```python
        v = spline.set_cyclic(selection, cyclic, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)
            - selection : Boolean
            - cyclic : Boolean## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SetSplineCyclic(geometry=self, selection=selection, cyclic=cyclic, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Geometry
            
        """

        return self.stack(nodes.SetSplineCyclic(geometry=self, selection=selection, cyclic=cyclic, label=node_label, node_color=node_color))

    def set_resolution(self, selection=None, resolution=None, node_label = None, node_color = None):
        """ > Node: SetSplineResolution
          
        <sub>go to: top index
        blender ref GeometryNodeSetSplineResolution
        node ref Set Spline Resolution </sub>
                                  
        ```python
        v = spline.set_resolution(selection, resolution, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)
            - selection : Boolean
            - resolution : Integer## Parameters
            - node_label : None
            - node_color : None
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.SetSplineResolution(geometry=self, selection=selection, resolution=resolution, label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Geometry
            
        """

        return self.stack(nodes.SetSplineResolution(geometry=self, selection=selection, resolution=resolution, label=node_label, node_color=node_color))

    def duplicate_splines(self, selection=None, amount=None, node_label = None, node_color = None):
        """ > Node: DuplicateElements
          
        <sub>go to: top index
        blender ref GeometryNodeDuplicateElements
        node ref Duplicate Elements </sub>
                                  
        ```python
        v = spline.duplicate_splines(selection, amount, node_label = None, node_color = None)
        ```
    

        Arguments
        ---------
            ## Sockets
            - geometry : Geometry (self)
            - selection : Boolean
            - amount : Integer## Parameters
            - node_label : None
            - node_color : None## Fixed parameters
            - domain : 'SPLINE'
    

        Node creation
        -------------
            ```python
            from geondes import nodes
            nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='SPLINE', label=node_label, node_color=node_color)
            ```
    

        Returns
        -------
            Sockets [geometry (Geometry), duplicate_index (Integer)]
            
        """

        return nodes.DuplicateElements(geometry=self, selection=selection, amount=amount, domain='SPLINE', label=node_label, node_color=node_color)


