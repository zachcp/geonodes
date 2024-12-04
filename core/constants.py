#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024/07/26

@author: alain

$ DOC hidden

-----------------------------------------------------
Scripting Geometry Nodes
-----------------------------------------------------

module : constants
------------------
- declare constants used in the script module

updates
-------
- creation : 2024/07/23
- update : 2024/09/04
"""

# ====================================================================================================
# Version

version = (3, 0, 0)
blender_version = (4, 2, 0)

# ====================================================================================================
# Correspondance between NodeSocket.type and type(NodeSocket)
# This list is automatically built from Blender with
# blendertree.gen_SOCKET_TYPES(tree_type)

SOCKET_TYPES = {
    'BOOLEAN':      ['NodeSocketBool'],
    'COLLECTION':   ['NodeSocketCollection'],
    'CUSTOM':       ['NodeSocketVirtual'],
    'GEOMETRY':     ['NodeSocketGeometry'],
    'IMAGE':        ['NodeSocketImage'],
    'INT':          ['NodeSocketInt',
                     'NodeSocketIntUnsigned'],
    'MATERIAL':     ['NodeSocketMaterial'],
    'MATRIX':       ['NodeSocketMatrix'],
    'MENU':         ['NodeSocketMenu'],
    'OBJECT':       ['NodeSocketObject'],
    'RGBA':         ['NodeSocketColor'],
    'ROTATION':     ['NodeSocketRotation'],
    'STRING':       ['NodeSocketString'],
    'VALUE':        ['NodeSocketFloatFactor',
                     'NodeSocketFloatAngle',
                     'NodeSocketFloat',
                     'NodeSocketFloatDistance'],
    'VECTOR':       ['NodeSocketVectorEuler',
                     'NodeSocketVector',
                     'NodeSocketVectorXYZ',
                     'NodeSocketVectorTranslation'],
    }

SOCKET_SUBTYPES = {
    'NodeSocketBool'                : ('NodeSocketBool',        'NONE'),
    'NodeSocketCollection'          : ('NodeSocketCollection',  'NONE'),
    'NodeSocketVirtual'             : ('NodeSocketVirtual',     'NONE'),
    'NodeSocketGeometry'            : ('NodeSocketGeometry',    'NONE'),
    'NodeSocketImage'               : ('NodeSocketImage',       'NONE'),
    'NodeSocketInt'                 : ('NodeSocketInt',         'NONE'),
    'NodeSocketIntUnsigned'         : ('NodeSocketInt',         'NONE'),
    'NodeSocketMaterial'            : ('NodeSocketMaterial',    'NONE'),
    'NodeSocketMatrix'              : ('NodeSocketMatrix',      'NONE'),
    'NodeSocketMenu'                : ('NodeSocketMenu',        'NONE'),
    'NodeSocketObject'              : ('NodeSocketObject',      'NONE'),
    'NodeSocketColor'               : ('NodeSocketColor',       'NONE'),
    'NodeSocketRotation'            : ('NodeSocketRotation',    'NONE'),
    'NodeSocketString'              : ('NodeSocketString',      'NONE'),
    'NodeSocketFloatFactor'         : ('NodeSocketFloat',       'FACTOR'),
    'NodeSocketFloatAngle'          : ('NodeSocketFloat',       'ANGLE'),
    'NodeSocketFloatTime'           : ('NodeSocketFloat',       'TIME'),
    'NodeSocketFloat'               : ('NodeSocketFloat',       'NONE'),
    'NodeSocketFloatDistance'       : ('NodeSocketFloat',       'DISTANCE'),
    'NodeSocketVectorEuler'         : ('NodeSocketVector',      'EULER'),
    'NodeSocketVector'              : ('NodeSocketVector',      'NONE'),
    'NodeSocketVectorXYZ'           : ('NodeSocketVector',      'XYZ'),
    'NodeSocketVectorTranslation'   : ('NodeSocketVector',      'TRANSLATION'),
}


DATA_TYPES = {
    'VALUE'      : 'FLOAT',
    'INT'        : 'INT',
    'VECTOR'     : 'FLOAT_VECTOR',
    'RGBA'       : 'FLOAT_COLOR',
    'BOOLEAN'    : 'BOOLEAN',
    'MATRIX'     : 'FLOAT4X4',
    'ROTATION'   : 'QUATERNION',

    'BYTE_COLOR' : 'BYTE_COLOR',
    'FLOAT2'     : 'FLOAT2',
    'INT8'       : 'INT8',
}

INPUT_TYPES = {
    'VALUE'         : 'FLOAT',
    'INT'           : 'INT',
    'BOOLEAN'       : 'BOOLEAN',
    'VECTOR'        : 'VECTOR',
    'ROTATION'      : 'ROTATION',
    'MATRIX'        : 'MATRIX',
    'STRING'        : 'STRING',
    'MENU'          : 'MENU',
    'RGBA'          : 'RGBA',
    'OBJECT'        : 'OBJECT',
    'IMAGE'         : 'IMAGE',
    'GEOMETRY'      : 'GEOMETRY',
    'COLLECTION'    : 'COLLECTION',
    'MATERIAL'      : 'MATERIAL',

    'SHADER'        : 'SHADER',
}

CLASS_NAMES = {
    'VALUE'         : 'Float',
    'INT'           : 'Integer',
    'BOOLEAN'       : 'Boolean',
    'VECTOR'        : 'Vector',
    'ROTATION'      : 'Rotation',
    'MATRIX'        : 'Matrix',
    'STRING'        : 'String',
    'MENU'          : 'Menu',
    'RGBA'          : 'Color',
    'OBJECT'        : 'Object',
    'IMAGE'         : 'Image',
    'GEOMETRY'      : 'Geometry',
    'COLLECTION'    : 'Collection',
    'MATERIAL'      : 'Material',

    'SHADER'        : 'Shader',
}

# =============================================================================================================================
# Valid types

VALID_SOCKET_TYPES = {
    'GeometryNodeTree': ['BOOLEAN', 'COLLECTION', 'CUSTOM', 'GEOMETRY', 'IMAGE', 'INT', 'MATERIAL', 'MATRIX', 'MENU',
                         'OBJECT', 'RGBA', 'ROTATION', 'STRING', 'VALUE', 'VECTOR'],
    'ShaderNodeTree': ['CUSTOM', 'RGBA', 'ROTATION', 'SHADER', 'STRING', 'VALUE', 'VECTOR'],
}

# =============================================================================================================================
# Array type combination

ARRAY_TYPES = {
    'VECTOR'  : {'shape': (3,),  'combine': 'Combine XYZ',    'init': 'Vector',   'param': 'vector'},
    'ROTATION': {'shape': (3,),  'combine': 'Combine XYZ',    'init': 'Rotation', 'param': 'rotation'},
    'RGBA'    : {'shape': (4,),  'combine': 'Combine Color',  'init': 'Color',    'param': 'color'},
    'MATRIX'  : {'shape': (16,), 'combine': 'Combine Matrix', 'init': None},
}

# =============================================================================================================================

TOOL_ONLY = (
    '3D Cursor',
    'Mouse Position',
    'Viewport Transform',
    'Active Element',
    'Selection',
    'Set Selection',
    'Face Set',
    'Set Face Set',
)

MODIFIER_ONLY = (
    'Simulation Input',
    'Viewer',
)

# =============================================================================================================================
# Node names : one dictionary per tree type
# Generated by:
# blendertree.gen_NODE_NAMES(tree_type)

NODE_NAMES = {
    'GeometryNodeTree': {
        #253 NODE NAMES for GeometryNodeTree
        'align euler to vector'   : 'FunctionNodeAlignEulerToVector',
        'align rotation to vector' : 'FunctionNodeAlignRotationToVector',
        'axes to rotation'        : 'FunctionNodeAxesToRotation',
        'axis angle to rotation'  : 'FunctionNodeAxisAngleToRotation',
        'boolean math'            : 'FunctionNodeBooleanMath',
        'combine color'           : 'FunctionNodeCombineColor',
        'combine matrix'          : 'FunctionNodeCombineMatrix',
        'combine transform'       : 'FunctionNodeCombineTransform',
        'compare'                 : 'FunctionNodeCompare',
        'euler to rotation'       : 'FunctionNodeEulerToRotation',
        'float to integer'        : 'FunctionNodeFloatToInt',
        'boolean'                 : 'FunctionNodeInputBool',
        'color'                   : 'FunctionNodeInputColor',
        'integer'                 : 'FunctionNodeInputInt',
        'rotation'                : 'FunctionNodeInputRotation',
        'special characters'      : 'FunctionNodeInputSpecialCharacters',
        'string'                  : 'FunctionNodeInputString',
        'vector'                  : 'FunctionNodeInputVector',
        'invert matrix'           : 'FunctionNodeInvertMatrix',
        'invert rotation'         : 'FunctionNodeInvertRotation',
        'multiply matrices'       : 'FunctionNodeMatrixMultiply',
        'project point'           : 'FunctionNodeProjectPoint',
        'quaternion to rotation'  : 'FunctionNodeQuaternionToRotation',
        'random value'            : 'FunctionNodeRandomValue',
        'replace string'          : 'FunctionNodeReplaceString',
        'rotate euler'            : 'FunctionNodeRotateEuler',
        'rotate rotation'         : 'FunctionNodeRotateRotation',
        'rotate vector'           : 'FunctionNodeRotateVector',
        'rotation to axis angle'  : 'FunctionNodeRotationToAxisAngle',
        'rotation to euler'       : 'FunctionNodeRotationToEuler',
        'rotation to quaternion'  : 'FunctionNodeRotationToQuaternion',
        'separate color'          : 'FunctionNodeSeparateColor',
        'separate matrix'         : 'FunctionNodeSeparateMatrix',
        'separate transform'      : 'FunctionNodeSeparateTransform',
        'slice string'            : 'FunctionNodeSliceString',
        'string length'           : 'FunctionNodeStringLength',
        'transform direction'     : 'FunctionNodeTransformDirection',
        'transform point'         : 'FunctionNodeTransformPoint',
        'transpose matrix'        : 'FunctionNodeTransposeMatrix',
        'value to string'         : 'FunctionNodeValueToString',
        'accumulate field'        : 'GeometryNodeAccumulateField',
        'domain size'             : 'GeometryNodeAttributeDomainSize',
        'attribute statistic'     : 'GeometryNodeAttributeStatistic',
        'bake'                    : 'GeometryNodeBake',
        'blur attribute'          : 'GeometryNodeBlurAttribute',
        'bounding box'            : 'GeometryNodeBoundBox',
        'capture attribute'       : 'GeometryNodeCaptureAttribute',
        'collection info'         : 'GeometryNodeCollectionInfo',
        'convex hull'             : 'GeometryNodeConvexHull',
        'corners of edge'         : 'GeometryNodeCornersOfEdge',
        'corners of face'         : 'GeometryNodeCornersOfFace',
        'corners of vertex'       : 'GeometryNodeCornersOfVertex',
        'arc'                     : 'GeometryNodeCurveArc',
        'endpoint selection'      : 'GeometryNodeCurveEndpointSelection',
        'handle type selection'   : 'GeometryNodeCurveHandleTypeSelection',
        'curve length'            : 'GeometryNodeCurveLength',
        'curve of point'          : 'GeometryNodeCurveOfPoint',
        'bézier segment'          : 'GeometryNodeCurvePrimitiveBezierSegment',
        'curve circle'            : 'GeometryNodeCurvePrimitiveCircle',
        'curve line'              : 'GeometryNodeCurvePrimitiveLine',
        'quadrilateral'           : 'GeometryNodeCurvePrimitiveQuadrilateral',
        'quadratic bézier'        : 'GeometryNodeCurveQuadraticBezier',
        'set handle type'         : 'GeometryNodeCurveSetHandles',
        'spiral'                  : 'GeometryNodeCurveSpiral',
        'set spline type'         : 'GeometryNodeCurveSplineType',
        'star'                    : 'GeometryNodeCurveStar',
        'curve to mesh'           : 'GeometryNodeCurveToMesh',
        'curve to points'         : 'GeometryNodeCurveToPoints',
        'deform curves on surface' : 'GeometryNodeDeformCurvesOnSurface',
        'delete geometry'         : 'GeometryNodeDeleteGeometry',
        'distribute points in grid' : 'GeometryNodeDistributePointsInGrid',
        'distribute points in volume' : 'GeometryNodeDistributePointsInVolume',
        'distribute points on faces' : 'GeometryNodeDistributePointsOnFaces',
        'dual mesh'               : 'GeometryNodeDualMesh',
        'duplicate elements'      : 'GeometryNodeDuplicateElements',
        'edge paths to curves'    : 'GeometryNodeEdgePathsToCurves',
        'edge paths to selection' : 'GeometryNodeEdgePathsToSelection',
        'edges of corner'         : 'GeometryNodeEdgesOfCorner',
        'edges of vertex'         : 'GeometryNodeEdgesOfVertex',
        'edges to face groups'    : 'GeometryNodeEdgesToFaceGroups',
        'extrude mesh'            : 'GeometryNodeExtrudeMesh',
        'face of corner'          : 'GeometryNodeFaceOfCorner',
        'evaluate at index'       : 'GeometryNodeFieldAtIndex',
        'evaluate on domain'      : 'GeometryNodeFieldOnDomain',
        'fill curve'              : 'GeometryNodeFillCurve',
        'fillet curve'            : 'GeometryNodeFilletCurve',
        'flip faces'              : 'GeometryNodeFlipFaces',
        'geometry to instance'    : 'GeometryNodeGeometryToInstance',
        'get named grid'          : 'GeometryNodeGetNamedGrid',
        'grid to mesh'            : 'GeometryNodeGridToMesh',
        'group'                   : 'GeometryNodeGroup',
        'image info'              : 'GeometryNodeImageInfo',
        'image texture'           : 'GeometryNodeImageTexture',
        'index of nearest'        : 'GeometryNodeIndexOfNearest',
        'index switch'            : 'GeometryNodeIndexSwitch',
        'active camera'           : 'GeometryNodeInputActiveCamera',
        'curve handle positions'  : 'GeometryNodeInputCurveHandlePositions',
        'curve tilt'              : 'GeometryNodeInputCurveTilt',
        'is edge smooth'          : 'GeometryNodeInputEdgeSmooth',
        'id'                      : 'GeometryNodeInputID',
        'image'                   : 'GeometryNodeInputImage',
        'index'                   : 'GeometryNodeInputIndex',
        'instance rotation'       : 'GeometryNodeInputInstanceRotation',
        'instance scale'          : 'GeometryNodeInputInstanceScale',
        'material'                : 'GeometryNodeInputMaterial',
        'material index'          : 'GeometryNodeInputMaterialIndex',
        'edge angle'              : 'GeometryNodeInputMeshEdgeAngle',
        'edge neighbors'          : 'GeometryNodeInputMeshEdgeNeighbors',
        'edge vertices'           : 'GeometryNodeInputMeshEdgeVertices',
        'face area'               : 'GeometryNodeInputMeshFaceArea',
        'is face planar'          : 'GeometryNodeInputMeshFaceIsPlanar',
        'face neighbors'          : 'GeometryNodeInputMeshFaceNeighbors',
        'mesh island'             : 'GeometryNodeInputMeshIsland',
        'vertex neighbors'        : 'GeometryNodeInputMeshVertexNeighbors',
        'named attribute'         : 'GeometryNodeInputNamedAttribute',
        'named layer selection'   : 'GeometryNodeInputNamedLayerSelection',
        'normal'                  : 'GeometryNodeInputNormal',
        'position'                : 'GeometryNodeInputPosition',
        'radius'                  : 'GeometryNodeInputRadius',
        'scene time'              : 'GeometryNodeInputSceneTime',
        'is face smooth'          : 'GeometryNodeInputShadeSmooth',
        'shortest edge paths'     : 'GeometryNodeInputShortestEdgePaths',
        'is spline cyclic'        : 'GeometryNodeInputSplineCyclic',
        'spline resolution'       : 'GeometryNodeInputSplineResolution',
        'curve tangent'           : 'GeometryNodeInputTangent',
        'instance on points'      : 'GeometryNodeInstanceOnPoints',
        'instance transform'      : 'GeometryNodeInstanceTransform',
        'instances to points'     : 'GeometryNodeInstancesToPoints',
        'interpolate curves'      : 'GeometryNodeInterpolateCurves',
        'is viewport'             : 'GeometryNodeIsViewport',
        'join geometry'           : 'GeometryNodeJoinGeometry',
        'material selection'      : 'GeometryNodeMaterialSelection',
        'menu switch'             : 'GeometryNodeMenuSwitch',
        'merge by distance'       : 'GeometryNodeMergeByDistance',
        'mesh boolean'            : 'GeometryNodeMeshBoolean',
        'mesh circle'             : 'GeometryNodeMeshCircle',
        'cone'                    : 'GeometryNodeMeshCone',
        'cube'                    : 'GeometryNodeMeshCube',
        'cylinder'                : 'GeometryNodeMeshCylinder',
        'face group boundaries'   : 'GeometryNodeMeshFaceSetBoundaries',
        'grid'                    : 'GeometryNodeMeshGrid',
        'ico sphere'              : 'GeometryNodeMeshIcoSphere',
        'mesh line'               : 'GeometryNodeMeshLine',
        'mesh to curve'           : 'GeometryNodeMeshToCurve',
        'mesh to density grid'    : 'GeometryNodeMeshToDensityGrid',
        'mesh to points'          : 'GeometryNodeMeshToPoints',
        'mesh to sdf grid'        : 'GeometryNodeMeshToSDFGrid',
        'mesh to volume'          : 'GeometryNodeMeshToVolume',
        'uv sphere'               : 'GeometryNodeMeshUVSphere',
        'object info'             : 'GeometryNodeObjectInfo',
        'offset corner in face'   : 'GeometryNodeOffsetCornerInFace',
        'offset point in curve'   : 'GeometryNodeOffsetPointInCurve',
        'points'                  : 'GeometryNodePoints',
        'points of curve'         : 'GeometryNodePointsOfCurve',
        'points to curves'        : 'GeometryNodePointsToCurves',
        'points to sdf grid'      : 'GeometryNodePointsToSDFGrid',
        'points to vertices'      : 'GeometryNodePointsToVertices',
        'points to volume'        : 'GeometryNodePointsToVolume',
        'geometry proximity'      : 'GeometryNodeProximity',
        'raycast'                 : 'GeometryNodeRaycast',
        'realize instances'       : 'GeometryNodeRealizeInstances',
        'remove named attribute'  : 'GeometryNodeRemoveAttribute',
        'repeat input'            : 'GeometryNodeRepeatInput',
        'repeat output'           : 'GeometryNodeRepeatOutput',
        'replace material'        : 'GeometryNodeReplaceMaterial',
        'resample curve'          : 'GeometryNodeResampleCurve',
        'reverse curve'           : 'GeometryNodeReverseCurve',
        'rotate instances'        : 'GeometryNodeRotateInstances',
        'sdf grid boolean'        : 'GeometryNodeSDFGridBoolean',
        'sample curve'            : 'GeometryNodeSampleCurve',
        'sample grid'             : 'GeometryNodeSampleGrid',
        'sample grid index'       : 'GeometryNodeSampleGridIndex',
        'sample index'            : 'GeometryNodeSampleIndex',
        'sample nearest'          : 'GeometryNodeSampleNearest',
        'sample nearest surface'  : 'GeometryNodeSampleNearestSurface',
        'sample uv surface'       : 'GeometryNodeSampleUVSurface',
        'scale elements'          : 'GeometryNodeScaleElements',
        'scale instances'         : 'GeometryNodeScaleInstances',
        'self object'             : 'GeometryNodeSelfObject',
        'separate components'     : 'GeometryNodeSeparateComponents',
        'separate geometry'       : 'GeometryNodeSeparateGeometry',
        'set handle positions'    : 'GeometryNodeSetCurveHandlePositions',
        'set curve normal'        : 'GeometryNodeSetCurveNormal',
        'set curve radius'        : 'GeometryNodeSetCurveRadius',
        'set curve tilt'          : 'GeometryNodeSetCurveTilt',
        'set id'                  : 'GeometryNodeSetID',
        'set instance transform'  : 'GeometryNodeSetInstanceTransform',
        'set material'            : 'GeometryNodeSetMaterial',
        'set material index'      : 'GeometryNodeSetMaterialIndex',
        'set point radius'        : 'GeometryNodeSetPointRadius',
        'set position'            : 'GeometryNodeSetPosition',
        'set shade smooth'        : 'GeometryNodeSetShadeSmooth',
        'set spline cyclic'       : 'GeometryNodeSetSplineCyclic',
        'set spline resolution'   : 'GeometryNodeSetSplineResolution',
        'simulation input'        : 'GeometryNodeSimulationInput',
        'simulation output'       : 'GeometryNodeSimulationOutput',
        'sort elements'           : 'GeometryNodeSortElements',
        'spline length'           : 'GeometryNodeSplineLength',
        'spline parameter'        : 'GeometryNodeSplineParameter',
        'split edges'             : 'GeometryNodeSplitEdges',
        'split to instances'      : 'GeometryNodeSplitToInstances',
        'store named attribute'   : 'GeometryNodeStoreNamedAttribute',
        'store named grid'        : 'GeometryNodeStoreNamedGrid',
        'join strings'            : 'GeometryNodeStringJoin',
        'string to curves'        : 'GeometryNodeStringToCurves',
        'subdivide curve'         : 'GeometryNodeSubdivideCurve',
        'subdivide mesh'          : 'GeometryNodeSubdivideMesh',
        'subdivision surface'     : 'GeometryNodeSubdivisionSurface',
        'switch'                  : 'GeometryNodeSwitch',
        '3d cursor'               : 'GeometryNodeTool3DCursor',
        'active element'          : 'GeometryNodeToolActiveElement',
        'face set'                : 'GeometryNodeToolFaceSet',
        'mouse position'          : 'GeometryNodeToolMousePosition',
        'selection'               : 'GeometryNodeToolSelection',
        'set face set'            : 'GeometryNodeToolSetFaceSet',
        'set selection'           : 'GeometryNodeToolSetSelection',
        'transform geometry'      : 'GeometryNodeTransform',
        'translate instances'     : 'GeometryNodeTranslateInstances',
        'triangulate'             : 'GeometryNodeTriangulate',
        'trim curve'              : 'GeometryNodeTrimCurve',
        'pack uv islands'         : 'GeometryNodeUVPackIslands',
        'uv unwrap'               : 'GeometryNodeUVUnwrap',
        'vertex of corner'        : 'GeometryNodeVertexOfCorner',
        'viewer'                  : 'GeometryNodeViewer',
        'viewport transform'      : 'GeometryNodeViewportTransform',
        'volume cube'             : 'GeometryNodeVolumeCube',
        'volume to mesh'          : 'GeometryNodeVolumeToMesh',
        'frame'                   : 'NodeFrame',
        'group input'             : 'NodeGroupInput',
        'group output'            : 'NodeGroupOutput',
        'reroute'                 : 'NodeReroute',
        'blackbody'               : 'ShaderNodeBlackbody',
        'clamp'                   : 'ShaderNodeClamp',
        'combine xyz'             : 'ShaderNodeCombineXYZ',
        'float curve'             : 'ShaderNodeFloatCurve',
        'map range'               : 'ShaderNodeMapRange',
        'math'                    : 'ShaderNodeMath',
        'mix'                     : 'ShaderNodeMix',
        'rgb curves'              : 'ShaderNodeRGBCurve',
        'separate xyz'            : 'ShaderNodeSeparateXYZ',
        'brick texture'           : 'ShaderNodeTexBrick',
        'checker texture'         : 'ShaderNodeTexChecker',
        'gradient texture'        : 'ShaderNodeTexGradient',
        'magic texture'           : 'ShaderNodeTexMagic',
        'noise texture'           : 'ShaderNodeTexNoise',
        'voronoi texture'         : 'ShaderNodeTexVoronoi',
        'wave texture'            : 'ShaderNodeTexWave',
        'white noise texture'     : 'ShaderNodeTexWhiteNoise',
        'color ramp'              : 'ShaderNodeValToRGB',
        'value'                   : 'ShaderNodeValue',
        'vector curves'           : 'ShaderNodeVectorCurve',
        'vector math'             : 'ShaderNodeVectorMath',
        'vector rotate'           : 'ShaderNodeVectorRotate',

        # 4.3 new nodes
        'curves to grease pencil' : 'GeometryNodeCurvesToGreasePencil',
        'dial gizmo'              : 'GeometryNodeGizmoDial',
        'for each geometry element input' : 'GeometryNodeForeachGeometryElementInput',
        'for each geometry element output': 'GeometryNodeForeachGeometryElementOutput',
        'gabor texture'           : 'ShaderNodeTexGabor',
        'grease pencil to curves' : 'GeometryNodeGreasePencilToCurves',
        'hash value'              : 'FunctionNodeHashValue',
        'import obj'              : 'GeometryNodeImportOBJ',
        'import ply'              : 'GeometryNodeImportPLY',
        'import stl'              : 'GeometryNodeImportSTL',
        'integer math'            : 'FunctionNodeIntegerMath',
        'linear gizmo'            : 'GeometryNodeGizmoLinear',
        'matrix determinant'      : 'FunctionNodeMatrixDeterminant',
        'merge layers'            : 'GeometryNodeMergeLayers',
        'set geometry name'       : 'GeometryNodeSetGeometryName',
        'transform gizmo'         : 'GeometryNodeGizmoTransform',
        'warning'                 : 'GeometryNodeWarning',

        },
'ShaderNodeTree': {
    # 97 NODE NAMES for ShaderNodeTree
    'frame'                   : 'NodeFrame',
    'group input'             : 'NodeGroupInput',
    'group output'            : 'NodeGroupOutput',
    'reroute'                 : 'NodeReroute',
    'add shader'              : 'ShaderNodeAddShader',
    'ambient occlusion'       : 'ShaderNodeAmbientOcclusion',
    'attribute'               : 'ShaderNodeAttribute',
    'background'              : 'ShaderNodeBackground',
    'bevel'                   : 'ShaderNodeBevel',
    'blackbody'               : 'ShaderNodeBlackbody',
    'brightness/contrast'     : 'ShaderNodeBrightContrast',
    'glossy bsdf'             : 'ShaderNodeBsdfAnisotropic',
    'diffuse bsdf'            : 'ShaderNodeBsdfDiffuse',
    'glass bsdf'              : 'ShaderNodeBsdfGlass',
    'hair bsdf'               : 'ShaderNodeBsdfHair',
    'principled hair bsdf'    : 'ShaderNodeBsdfHairPrincipled',
    'principled bsdf'         : 'ShaderNodeBsdfPrincipled',
    'ray portal bsdf'         : 'ShaderNodeBsdfRayPortal',
    'refraction bsdf'         : 'ShaderNodeBsdfRefraction',
    'sheen bsdf'              : 'ShaderNodeBsdfSheen',
    'toon bsdf'               : 'ShaderNodeBsdfToon',
    'translucent bsdf'        : 'ShaderNodeBsdfTranslucent',
    'transparent bsdf'        : 'ShaderNodeBsdfTransparent',
    'bump'                    : 'ShaderNodeBump',
    'camera data'             : 'ShaderNodeCameraData',
    'clamp'                   : 'ShaderNodeClamp',
    'combine color'           : 'ShaderNodeCombineColor',
    'combine xyz'             : 'ShaderNodeCombineXYZ',
    'displacement'            : 'ShaderNodeDisplacement',
    'specular bsdf'           : 'ShaderNodeEeveeSpecular',
    'emission'                : 'ShaderNodeEmission',
    'float curve'             : 'ShaderNodeFloatCurve',
    'fresnel'                 : 'ShaderNodeFresnel',
    'gamma'                   : 'ShaderNodeGamma',
    'group'                   : 'ShaderNodeGroup',
    'curves info'             : 'ShaderNodeHairInfo',
    'holdout'                 : 'ShaderNodeHoldout',
    'hue/saturation/value'    : 'ShaderNodeHueSaturation',
    'invert color'            : 'ShaderNodeInvert',
    'layer weight'            : 'ShaderNodeLayerWeight',
    'light falloff'           : 'ShaderNodeLightFalloff',
    'light path'              : 'ShaderNodeLightPath',
    'map range'               : 'ShaderNodeMapRange',
    'mapping'                 : 'ShaderNodeMapping',
    'math'                    : 'ShaderNodeMath',
    'mix'                     : 'ShaderNodeMix',
    'mix shader'              : 'ShaderNodeMixShader',
    'geometry'                : 'ShaderNodeNewGeometry',
    'normal'                  : 'ShaderNodeNormal',
    'normal map'              : 'ShaderNodeNormalMap',
    'object info'             : 'ShaderNodeObjectInfo',
    'aov output'              : 'ShaderNodeOutputAOV',
    'light output'            : 'ShaderNodeOutputLight',
    'line style output'       : 'ShaderNodeOutputLineStyle',
    'material output'         : 'ShaderNodeOutputMaterial',
    'world output'            : 'ShaderNodeOutputWorld',
    'particle info'           : 'ShaderNodeParticleInfo',
    'point info'              : 'ShaderNodePointInfo',
    'rgb'                     : 'ShaderNodeRGB',
    'rgb curves'              : 'ShaderNodeRGBCurve',
    'rgb to bw'               : 'ShaderNodeRGBToBW',
    'script'                  : 'ShaderNodeScript',
    'separate color'          : 'ShaderNodeSeparateColor',
    'separate xyz'            : 'ShaderNodeSeparateXYZ',
    'shader to rgb'           : 'ShaderNodeShaderToRGB',
    'subsurface scattering'   : 'ShaderNodeSubsurfaceScattering',
    'tangent'                 : 'ShaderNodeTangent',
    'brick texture'           : 'ShaderNodeTexBrick',
    'checker texture'         : 'ShaderNodeTexChecker',
    'texture coordinate'      : 'ShaderNodeTexCoord',
    'environment texture'     : 'ShaderNodeTexEnvironment',
    'gradient texture'        : 'ShaderNodeTexGradient',
    'ies texture'             : 'ShaderNodeTexIES',
    'image texture'           : 'ShaderNodeTexImage',
    'magic texture'           : 'ShaderNodeTexMagic',
    'noise texture'           : 'ShaderNodeTexNoise',
    'point density'           : 'ShaderNodeTexPointDensity',
    'sky texture'             : 'ShaderNodeTexSky',
    'voronoi texture'         : 'ShaderNodeTexVoronoi',
    'wave texture'            : 'ShaderNodeTexWave',
    'white noise texture'     : 'ShaderNodeTexWhiteNoise',
    'uv along stroke'         : 'ShaderNodeUVAlongStroke',
    'uv map'                  : 'ShaderNodeUVMap',
    'color ramp'              : 'ShaderNodeValToRGB',
    'value'                   : 'ShaderNodeValue',
    'vector curves'           : 'ShaderNodeVectorCurve',
    'vector displacement'     : 'ShaderNodeVectorDisplacement',
    'vector math'             : 'ShaderNodeVectorMath',
    'vector rotate'           : 'ShaderNodeVectorRotate',
    'vector transform'        : 'ShaderNodeVectorTransform',
    'color attribute'         : 'ShaderNodeVertexColor',
    'volume absorption'       : 'ShaderNodeVolumeAbsorption',
    'volume info'             : 'ShaderNodeVolumeInfo',
    'principled volume'       : 'ShaderNodeVolumePrincipled',
    'volume scatter'          : 'ShaderNodeVolumeScatter',
    'wavelength'              : 'ShaderNodeWavelength',
    'wireframe'               : 'ShaderNodeWireframe',
    # Blender 4.3
    'metallic bsdf'           : 'ShaderNodeBsdfMetallic',
    'gabor texture'           : 'ShaderNodeTexGabor',
    },
}
