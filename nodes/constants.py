#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 07:14:33 2024

@author: alain

-----------------------------------------------------
geonodes module
- Generates nodes with python
- Use numpy to manage vertices
-----------------------------------------------------

module : constants
------------------
- low level constants uses by dynamic nodes generator
- dictionaries used to register the class created dynamically

update : 2024/02/17
"""

from pprint import pprint

# ====================================================================================================
# Version

version = (2, 0, 0)
blender = (4, 1, 0)

bldoc_node_bl_idname = "https://docs.blender.org/api/current/bpy.types"

bldoc_nodes = {
    'GeometryNodeTree'   : 'https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/blur_attribute.html',
    'ShaderNodeTree'     : '',
    'CompositorNodeTree' : '',
    #'TextureNodeTree'    : '',
    }

# =============================================================================================================================
# One tree can be edited at a time.
# The current tree is stacked
# The method constants.current_tree() returns the current tree

TREE_STACK  = []
FRAME_STACK = []

def get_tree_type():
    return None if len(TREE_STACK) == 0 else TREE_STACK[-1].TREE_TYPE

def current_tree(bl_idname=None):
    if len(TREE_STACK):
        return TREE_STACK[-1]
    else:
        raise Exception(f"Tree stack is empty: not Tree has been initialized. Impossible to create node '{bl_idname}'.")
        
def current_tree_type(bl_idname=None):
    return type(current_tree(bl_idname).btree).__name__

def dump_stack(title="Dump stack"):
    print(f"{title} :", len(TREE_STACK))
    for tree in TREE_STACK:
        print(tree)
    print()
    
# ====================================================================================================
# System Colors

NODE_COLORS = {
    'property' : (.30, .30, .25),  # For nodes created by property
    'gen'      : (.20, .10, .05),  # For nodes generated by customization
    'operator' : (.24, .00, .48), # For nodes generated by operators
    }

# ====================================================================================================
# Standard node attribute names which are not properties
#
# TextureNodeTree is legacy and is not implemenetd

TREE_TYPES = [
    'GeometryNodeTree',
    'ShaderNodeTree', 
    'CompositorNodeTree', 
    'TextureNodeTree',
    ]

TREE_BL_IDS = {
    'GeoNodes'   : 'GeometryNodeTree',
    'Shader'     : 'ShaderNodeTree',
    'Compositor' : 'CompositorNodeTree',
    'Texture'    : 'TextureNodeTree',
    }

TREE_CLASS_NAMES = {
    'GeometryNodeTree'   : 'GeoNodes',
    'ShaderNodeTree'     : 'Shader',
    'CompositorNodeTree' : 'Compositor',
    'TextureNodeTree'    : 'Texture',
    }

# ====================================================================================================
# Standard node attribute names which are not properties

STANDARD_NODE_ATTRS = [
   '__doc__', '__module__', '__slots__', 'bl_description', 'bl_height_default', 'bl_height_max',
   'bl_height_min', 'bl_icon', 'bl_idname', 'bl_label', 'bl_rna', 'bl_static_type',
   'bl_width_default', 'bl_width_max', 'bl_width_min', 'color', 'dimensions', 'draw_buttons',
   'draw_buttons_ext', 'height', 'hide', 'input_template', 'inputs', 'internal_links',
   'is_registered_node_type', 'label', 'location', 'mute', 'name', 'output_template', 'outputs',
   'parent', 'poll', 'poll_instance', 'rna_type', 'select', 'show_options', 'show_preview',
   'show_texture', 'socket_value_update', 'type', 'update', 'use_custom_color',
   'width', 'width_hidden',
   'index_switch_items', 'enum_definition']

# ====================================================================================================
# Gives the Blender socket type from a python type or a node socket type

TYPE_TO_SOCKET_BL_ID = {  # OLD = BLENDER_SOCKET_CLASSES
    bool            : 'NodeSocketBool',
    int             : 'NodeSocketInt',
    float           : 'NodeSocketFloat',
    str             : 'NodeSocketString',
    
    'BOOLEAN'       : 'NodeSocketBool',
    'INT'           : 'NodeSocketInt',
    'FLOAT'         : 'NodeSocketFloat',
    'VECTOR'        : 'NodeSocketVector',
    'COLOR'         : 'NodeSocketColor',
    'STRING'        : 'NodeSocketString',
    
    'GEOMETRY'      : 'NodeSocketGeometry',
    
    'COLLECTION'    : 'NodeSocketCollection',
    'IMAGE'         : 'NodeSocketImage',
    'MATERIAL'      : 'NodeSocketMaterial',
    'OBJECT'        : 'NodeSocketObject',
    'TEXTURE'       : 'NodeSocketTexture',
    
    'MENU'          : 'NodeSocketMenu',
    }

# ====================================================================================================
# Default (more frequent !) socket name per type

SOCKET_CLASS_DEFAULT_SOCKET_NAME = {
    'VALUE'      : 'value', 
    'INT'        : 'integer', 
    'BOOLEAN'    : 'boolean', 
    'VECTOR'     : 'vector', 
    'ROTATION'   : 'rotation', 
    'STRING'     : 'string', 
    'RGBA'       : 'color', 
    'SHADER'     : 'shader',
    'OBJECT'     : 'object', 
    'IMAGE'      : 'image', 
    'GEOMETRY'   : 'geometry', 
    'COLLECTION' : 'collection', 
    'TEXTURE'    : 'texture', 
    'MATERIAL'   : 'material',  
    }

DATA_TYPE_TO_SOCKET_CLASS_NAME = { # DATA_TYPE_CLASSES
    'FLOAT'      : 'VALUE', 
    'INT'        : 'INT', 
    'BOOLEAN'    : 'BOOLEAN', 
    'VECTOR'     : 'VECTOR', 
    'ROTATION'   : 'ROTATION', 
    'STRING'     : 'STRING', 
    'RGBA'       : 'RGBA', 
    'OBJECT'     : 'OBJECT', 
    'IMAGE'      : 'IMAGE', 
    'GEOMETRY'   : 'GEOMETRY', 
    'COLLECTION' : 'COLLECTION', 
    'TEXTURE'    : 'TEXTURE', 
    'MATERIAL'   : 'MATERIAL',
    }

# Legacy

SOCKET_CLASS_NAME_SHORTCUTS = {
    'Custom'     : 'CUSTOM',
    'Float'      : 'VALUE', 
    'Int'        : 'INT', 
    'Bool'       : 'BOOLEAN', 
    'Vect'       : 'VECTOR', 
    'Rot'        : 'ROTATION', 
    'Str'        : 'STRING', 
    'Col'        : 'RGBA', 
    'Shader'     : 'SHADER',
    'Object'     : 'OBJECT', 
    'Img'        : 'IMAGE', 
    'Geometry'   : 'GEOMETRY', 
    'Collection' : 'COLLECTION', 
    'Texture'    : 'TEXTURE', 
    'Mat'        : 'MATERIAL', 
    }

# ====================================================================================================
# Nodes with in / out custom sockets

CUSTOM_INPUT_SOCKETS = [
    
    'ShaderNodeGroup',
    'CompositorNodeGroup',
    'GeometryNodeGroup',
    
    'GeometryNodeSimulationInput', 
    'GeometryNodeSimulationOutput',
    'GeometryNodeRepeatInput',
    'GeometryNodeRepeatOutput',
    
    'GeometryNodeMenuSwitch',
    ]

CUSTOM_OUTPUT_SOCKETS = [
    
    'ShaderNodeGroup',
    'CompositorNodeGroup',
    'GeometryNodeGroup', 
    
    'GeometryNodeSimulationInput', 
    'GeometryNodeSimulationOutput',
    'GeometryNodeRepeatInput',
    'GeometryNodeRepeatOutput',
    ]

# ====================================================================================================
# Nodes with virtual sockets (other input nodes and zones)

HAS_VIRTUAL_SOCKETS = {
    'GeometryNodeBake' : 'bake_items',
    }

# ---- Node with *args in header

USE_ARGS_NODES = [
    'GeometryNodeIndexSwitch',
    ]

# Include all output sockets, even the hidden ones

INCLUDE_HIDDEN_OUTPUT_SOCKETS = [
    'CompositorNodeRLayers',
    ]

NO_DOC_NODES = [
    'ShaderNodeGroup',
    'CompositorNodeGroup',
    'GeometryNodeGroup',
    
    'GeometryNodeSimulationInput', 
    'GeometryNodeSimulationOutput',
    'GeometryNodeRepeatInput',
    'GeometryNodeRepeatOutput',
    ]


# =============================================================================================================================
# The existing sockets for each tree type
#
# In case new sockets are created, a CAUTION message will be displayed by node_info.check_socket_bl_idnames


BL_ID_SOCKET_TO_TYPE = {
    'GeometryNodeTree' : {
             'NodeSocketBool'               : 'BOOLEAN',
             'NodeSocketCollection'         : 'COLLECTION',
             'NodeSocketColor'              : 'RGBA',
             'NodeSocketFloat'              : 'VALUE',
             'NodeSocketFloatAngle'         : 'VALUE',
             'NodeSocketFloatDistance'      : 'VALUE',
             'NodeSocketFloatFactor'        : 'VALUE',
             'NodeSocketGeometry'           : 'GEOMETRY',
             'NodeSocketImage'              : 'IMAGE',
             'NodeSocketInt'                : 'INT',
             'NodeSocketIntUnsigned'        : 'INT',
             'NodeSocketMaterial'           : 'MATERIAL',
             'NodeSocketObject'             : 'OBJECT',
             'NodeSocketRotation'           : 'ROTATION',
             'NodeSocketString'             : 'STRING',
             'NodeSocketTexture'            : 'TEXTURE',
             'NodeSocketVector'             : 'VECTOR',
             'NodeSocketVectorEuler'        : 'VECTOR',
             'NodeSocketVectorTranslation'  : 'VECTOR',
             'NodeSocketVectorXYZ'          : 'VECTOR',
             'NodeSocketVirtual'            : 'CUSTOM',
             'NodeSocketMenu'               : 'MENU',
        },
    'ShaderNodeTree' : {
             'NodeSocketColor'              : 'RGBA',
             'NodeSocketFloat'              : 'VALUE',
             'NodeSocketFloatAngle'         : 'VALUE',
             'NodeSocketFloatDistance'      : 'VALUE',
             'NodeSocketFloatFactor'        : 'VALUE',
             'NodeSocketFloatUnsigned'      : 'VALUE',
             'NodeSocketRotation'           : 'ROTATION',
             'NodeSocketShader'             : 'SHADER',
             'NodeSocketString'             : 'STRING',
             'NodeSocketVector'             : 'VECTOR',
             'NodeSocketVectorDirection'    : 'VECTOR',
             'NodeSocketVectorEuler'        : 'VECTOR',
             'NodeSocketVectorTranslation'  : 'VECTOR',
             'NodeSocketVectorXYZ'          : 'VECTOR',
             'NodeSocketVirtual'            : 'CUSTOM',
        },
    'CompositorNodeTree' : {
             'NodeSocketColor'              : 'RGBA',
             'NodeSocketFloat'              : 'VALUE',
             'NodeSocketFloatAngle'         : 'VALUE',
             'NodeSocketFloatFactor'        : 'VALUE',
             'NodeSocketFloatUnsigned'      : 'VALUE',
             'NodeSocketVector'             : 'VECTOR',
             'NodeSocketVectorDirection'    : 'VECTOR',
             'NodeSocketVectorTranslation'  : 'VECTOR',
             'NodeSocketVectorVelocity'     : 'VECTOR',
             'NodeSocketVectorXYZ'          : 'VECTOR',
             'NodeSocketVirtual'            : 'CUSTOM', 
        },
    'TextureNodeTree' : {
             'NodeSocketColor'              : 'RGBA',
             'NodeSocketFloat'              : 'VALUE',
             'NodeSocketFloatFactor'        : 'VALUE',
             'NodeSocketFloatUnsigned'      : 'VALUE',
             'NodeSocketVector'             : 'VECTOR',
             'NodeSocketVectorDirection'    : 'VECTOR',
             'NodeSocketVectorTranslation'  : 'VECTOR',
             'NodeSocketVectorXYZ'          : 'VECTOR',
             'NodeSocketVirtual'            : 'CUSTOM', 
        },
    }

def all_socket_classes(tree_type):
    types = set(BL_ID_SOCKET_TO_TYPE[tree_type].values())
    return list(types)
    #return {TYPE_TO_SOCKET_CLASS_NAME[tp]: tp for tp in types}


# =============================================================================================================================
# Trees dict
# The nodes
# - key    : tree_type
# - value  : Dynamic instance

TREES = {}

# =============================================================================================================================
# Nodes dict
# The nodes
# - key    : node bl_idname
# - value  : Dynamic instance

NODES = {tree_type: {} for tree_type in TREE_TYPES}

def get_node_class_name(tree_type, bl_idname):
    dyn = NODES[tree_type].get(bl_idname)
    if dyn is None:
        raise AttributeError(f"Node bl_idname {bl_idname} not found for tree type {tree_type}")
    else:
        return dyn.class_name

def get_node_class(tree_type, bl_idname):
    dyn = NODES[tree_type].get(bl_idname)
    if dyn is None:
        raise AttributeError(f"Node bl_idname {bl_idname} not found for tree type {tree_type}")
    else:
        return dyn.dyn_class
    
def print_node_bl_idnames(tree_type):
    for blid, dyn in NODES[tree_type].items():
        print(f"{dyn.node_info.class_name:20s}: {blid}")

# =============================================================================================================================
# Sockets dict
# The nodes
# - key    : socket class name
# - value  : Dynamic instance

SOCKETS = {tree_type: {} for tree_type in TREE_TYPES}

def get_socket_class_name(socket_type):
    return socket_type
    
    
    
    #class_name = DATA_TYPE_TO_SOCKET_CLASS_NAME.get(socket_type)
    class_name = TYPE_TO_SOCKET_CLASS_NAME.get(socket_type)
    if class_name is None:
        raise AttributeError(f"Unknwon socket type '{socket_type}' in {list(TYPE_TO_SOCKET_CLASS_NAME.keys())}")
    return class_name

def get_socket_class(socket_type):
    if len(TREE_STACK):
        tree_type = TREE_STACK[0].TREE_TYPE
        return SOCKETS[tree_type][socket_type].dyn_class
    
    
        tree_type = TREE_STACK[0].TREE_TYPE
        return SOCKETS[tree_type][get_socket_class_name(socket_type)].dyn_class
    else:
        return None
    
def get_socket_class_from_bl_idname(tree_type, bl_idname):
    return get_socket_class(BL_ID_SOCKET_TO_TYPE[tree_type][bl_idname])

# =============================================================================================================================
# Global dict
# Global functions and properties implemented at Tree level
# - key    : function or property name
# - value  : dynamic instance

GLOBAL = {tree_type: {} for tree_type in TREE_TYPES}

# =============================================================================================================================
# Cross references
# - key    : node class name
# - value  : dict of {key: socket class name, value: list of names}

CROSS_REF = {tree_type: {} for tree_type in TREE_TYPES}

def cross_ref(tree_type, node_class_name, target_class_name, name):
    
    # Node class name entry
    
    dct = CROSS_REF[tree_type].get(node_class_name)
    if dct is None:
        dct = {}
        CROSS_REF[tree_type][node_class_name] = dct
        
    # Socket class name entry
        
    if target_class_name is None:
        target_class_name = 'GLOBAL'
        
    names = dct.get(target_class_name)
    if names is None:
        names = []
        dct[target_class_name] = names
        
    names.append(name)
    
    #print("constants.cross_ref", target_class_name)
    
# =============================================================================================================================
# Reset    
    
def reset():
    
    for tree_type, dyn_tree in TREES.items():
        
        tree_class = dyn_tree.dyn_class
        
        # ----- Remove the node classes
        
        for bl_idname, dyn in NODES[tree_type].items():
            delattr(tree_class, dyn.node_info.class_name)
        NODES[tree_type].clear()

        # ----- Remove the socket classes
        
        for class_name in SOCKETS[tree_type].keys():
            delattr(tree_class, class_name)
        SOCKETS[tree_type].clear()

        # ----- Remove the global functions

        for name in GLOBAL[tree_type].keys():
            delattr(tree_class, name)
        GLOBAL[tree_type].clear()
        
        # ----- Clear the cross references
        
        CROSS_REF[tree_type].clear()
        
        # ----- Reinit the tree class
        
        tree_class.INIT = False
        
    # ----- Remove the trees
        
    TREES.clear()
    
    
    
# OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD OLD 

SOCKET_CLASS_DEFAULT_SOCKET_NAME_OLD = {
    'Float'      : 'value', 
    'Int'        : 'integer', 
    'Bool'       : 'boolean', 
    'Vect'       : 'vector', 
    'Rot'        : 'rotation', 
    'Str'        : 'string', 
    'Col'        : 'color', 
    'Shader'     : 'shader',
    'Object'     : 'object', 
    'Img'        : 'image', 
    'Geometry'   : 'geometry', 
    'Collection' : 'collection', 
    'Texture'    : 'texture', 
    'Mat'        : 'material',  
    }


TYPE_TO_SOCKET_CLASS_NAME_OLD = { # SOCKET_CLASS_NAMES
    'CUSTOM'     : 'Custom',
    'VALUE'      : 'Float', 
    'INT'        : 'Int', 
    'BOOLEAN'    : 'Bool', 
    'VECTOR'     : 'Vect', 
    'ROTATION'   : 'Rot', 
    'STRING'     : 'Str', 
    'RGBA'       : 'Col', 
    'SHADER'     : 'Shader',
    'OBJECT'     : 'Object', 
    'IMAGE'      : 'Img', 
    'GEOMETRY'   : 'Geometry', 
    'COLLECTION' : 'Collection', 
    'TEXTURE'    : 'Texture', 
    'MATERIAL'   : 'Mat', 
    }

TYPE_TO_SOCKET_CLASS_NAME_LEGACY = { # SOCKET_CLASS_NAMES
    'CUSTOM'     : 'CUSTOM',
    'VALUE'      : 'VALUE', 
    'INT'        : 'INT', 
    'BOOLEAN'    : 'BOOLEAN', 
    'VECTOR'     : 'VECTOR', 
    'ROTATION'   : 'ROTATION', 
    'STRING'     : 'STRING', 
    'RGBA'       : 'RGBA', 
    'SHADER'     : 'SHADER',
    'OBJECT'     : 'OBJECT', 
    'IMAGE'      : 'IMAGE', 
    'GEOMETRY'   : 'GEOMETRY', 
    'COLLECTION' : 'COLLECTION', 
    'TEXTURE'    : 'TEXTURE', 
    'MATERIAL'   : 'MATERIAL', 
    }

DATA_TYPE_TO_SOCKET_CLASS_NAME_OLD = { # DATA_TYPE_CLASSES
    'FLOAT'      : 'Float', 
    'INT'        : 'Int', 
    'BOOLEAN'    : 'Bool', 
    'VECTOR'     : 'Vect', 
    'ROTATION'   : 'Rot', 
    'STRING'     : 'Str', 
    'RGBA'       : 'Col', 
    'OBJECT'     : 'Object', 
    'IMAGE'      : 'Img', 
    'GEOMETRY'   : 'Geometry', 
    'COLLECTION' : 'Collection', 
    'TEXTURE'    : 'Texture', 
    'MATERIAL'   : 'Mat',
    }

# ====================================================================================================
# Constant nodes
# Nodes implemented as method
# b = tree.boolean(True)
"""
CONSTANT_NODES = {
    'Boolean':  'boolean',
    'Color':    'color',
    'Image':    'image',
    'Integer':  'integer',
    'Material': 'material',
    'String':   'string',
    'Value':    'value',
    'Vector':   'vector',
    }
"""

# ====================================================================================================
# Nodes which are not implemented as input nodes
"""
NO_INPUT_NODES = list(CONSTANT_NODES.keys()) + [
    'GroupOutput',
    'GroupInput',
    'SimulationInput',
    'Group',
    ]
"""


    
        
        
    
    
    
    
    
    
    
    
    
    
    
     
        
        
    
    
    
    
    








