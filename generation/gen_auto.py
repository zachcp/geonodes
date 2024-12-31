from pathlib import Path
import bpy

from . node_explore import NodeInfo

f            = 'func'
name         = 'func_name'
ret          = 'ret'
klass        = 'class_name'
cache        = 'cache'
parameters   = 'parameters'
domain_param = 'domain_param'
param_loop   = 'param_loop'
prefix       = 'prefix'
suffix       = 'suffix'
operation    = 'operation'
self_        = 'self_'
domain       = 'domain_value'
only_enabled = 'only_enabled'
rename       = 'rename'

setter       = 'setter'
getter       = 'getter'
in_socket    = 'in_socket'
in_prm       = 'in_parameter'
out_socket   = 'out_socket'
set_prm      = 'setter_params'
get_prm      = 'getter_params'
set_sock     = 'setter_sockets'
get_sock     = 'getter_sockets'


GEONODES = {
'Align Rotation to Vector' :    [{f: 'C', name: 'AlignToVector'},
                                 {f: 'C', name: 'AlignXToVector', parameters: {'axis': 'X'}},
                                 {f: 'C', name: 'AlignYToVector', parameters: {'axis': 'Y'}},
                                 {f: 'C', name: 'AlignZToVector', parameters: {'axis': 'Z'}},
                                 {name: 'align_toVector'},
                                 {name: 'align_x_to_vector', parameters: {'axis': 'X'}},
                                 {name: 'align_y_to_vector', parameters: {'axis': 'Y'}},
                                 {name: 'align_z_to_vector', parameters: {'axis': 'Z'}},
                                ],
'Axes to Rotation'   :          [{f: 'C',   name: 'FromAxes'},
                                 {f: 'C', name: 'FromXYAxes', parameters: {'primary_axis': 'X', 'secondary_axis': 'Y'}},
                                 {f: 'C', name: 'FromYXAxes', parameters: {'primary_axis': 'Y', 'secondary_axis': 'X'}},
                                 {f: 'C', name: 'FromXZAxes', parameters: {'primary_axis': 'X', 'secondary_axis': 'Z'}},
                                 {f: 'C', name: 'FromYZAxes', parameters: {'primary_axis': 'Z', 'secondary_axis': 'X'}},
                                 {f: 'C', name: 'FromYZAxes', parameters: {'primary_axis': 'Y', 'secondary_axis': 'Z'}},
                                 {f: 'C', name: 'FromZYAxes', parameters: {'primary_axis': 'Z', 'secondary_axis': 'Y'}},
                                ],
'Axis Angle to Rotation' :      [{f: 'C', name: 'FromAxisAngle'}],
'Boolean Math'       :          [{f: 'op', rename: {
                                        'and'      : 'band',
                                        'or'       : 'bor',
                                        'not'      : 'bnot',
                                        'nand'     : 'not_and',
                                }},
                                {f: 'math', rename: {
                                        'and'      : 'band',
                                        'or'       : 'bor',
                                        'not'      : 'bnot',
                                        'nand'     : 'not_and',
                                }},
                                ],
'Combine Color'      :          [{f: 'C', name: 'Combine', 'mode_loop': True}],
'Combine Matrix'     :          [{f: 'C', name: 'Combine'}],
'Combine Transform'  :          [{f: 'C', name: 'CombineTransform'}],
'Compare'            :          [{f: 'op', parameters: {'data_type': 'FLOAT', 'mode': 'ELEMENT'}},
                                 {f: 'op', parameters: {'data_type': 'INT', 'mode': 'ELEMENT'}},
                                 {f: 'op', parameters: {'data_type': 'VECTOR'}},
                                 {f: 'op', parameters: {'data_type': 'STRING', 'mode': 'ELEMENT'}},
                                 {f: 'op', parameters: {'data_type': 'RGBA', 'mode': 'ELEMENT'}},
                                ],
'Euler to Rotation'  :          [{f: 'C', name: 'FromEuler'}, {f: 'method', name: 'to_rotation'}],
'Float to Integer'   :          [{name: 'to_integer'}],
'Hash Value'         :          [{}],
'Boolean'            :          [{f: 'INIT'}],
'Color'              :          [{f: 'INIT'}],
'Integer'            :          [{f: 'INIT'}],
'Rotation'           :          [{f: 'INIT'}],
'Special Characters' :          [{f: 'get', klass: 'String', ret: 'NODE'},
                                 {f: 'get', name: 'line_break', klass: 'String'},
                                 {f: 'get', name: 'tab', klass: 'String', ret: 'tab'},
                                ],
'String'             :          [{f: 'INIT'}],
'Vector'             :          [{f: 'INIT'}],
'Integer Math'       :          [{f: 'op', rename: {
                                        'minimum'      : 'min',
                                        'maximum'      : 'max',
                                        'absolute'     : 'abs',
                                }},
                                {f: 'math', rename: {
                                        'minimum'      : 'imin',
                                        'maximum'      : 'imax',
                                        'absolute'     : 'iabs',
                                        'add'          : 'iadd',
                                        'subtract'     : 'isubtract',
                                        'multiply'     : 'imultiply',
                                        'divide'       : 'idivide',
                                        'multiply_add' : 'imultiply_add',
                                }},
                                ],
'Invert Matrix'      :          [{name: 'invert'}],
'Invert Rotation'    :          [{name: 'invert'}],
'Matrix Determinant' :          [{f: 'get',    name: 'determinant'}],
'Multiply Matrices'  :          [{name: 'multiply'}],
'Project Point'      :          [{self_: 'Transform'}],
'Quaternion to Rotation' :      [{f: 'C', name: 'FromQuaternion'}],
'Random Value'       :          [{f: 'C', name: 'Random'}],
'Replace String'     :          [{name: 'replace'}],
'Rotate Rotation'    :          [{name: 'rotate'},
                                 {param_loop: 'rotation_space', prefix: 'rotate_'},
                                ],
'Rotate Vector'      :          [{self_: 'Rotation'}],
'Rotation to Axis Angle' :      [{name: 'to_axis_angle'},
                                 {f: 'get', name: 'axis_angle', ret: 'TUPLE'},
                                ],
'Rotation to Euler'  :          [{name: 'to_euler'}],
'Rotation to Quaternion' :      [{name: 'to_quaternion'},
                                 {f: 'get', name: 'wxyz', ret: 'TUPLE'},
                                ],
'Separate Color'     :          [{f: 'get', name: 'separate', cache: True},
                                 {f: 'get', name:'rgb', ret: 'TUPLE', cache: True, parameters: {'mode': 'RGB'}},
                                 {f: 'get', name:'hsv', ret: 'TUPLE', cache: True, parameters: {'mode': 'HSV'}},
                                 {f: 'get', name:'hsv', ret: 'TUPLE', cache: True, parameters: {'mode': 'HSL'}},
                                 {f: 'get_out_loop', parameters: {'mode': 'HSL'}},
                                 {f: 'get_out_loop', parameters: {'mode': 'HSV'}},
                                 {f: 'get_out_loop', parameters: {'mode': 'RGB'}},
                                ],
'Separate Matrix'    :          [{f: 'get', name: 'separate', cache: True, ret: 'TUPLE'},
                                 {f: 'get_out_loop', prefix: ''},
                                ],
'Separate Transform' :          [{f: 'get', name: 'trs', ret: 'TUPLE'},
                                 {f: 'get_out_loop', prefix: ''},
                                ],
'Slice String'       :          [{name: 'slice'}],
'String Length'      :          [{f: 'get', name: 'length'}],
'Transform Direction' :         [{self_: 'Transform'}],
'Transform Point'    :          [{self_: 'Transform'}],
'Transpose Matrix'   :          [{name: 'transpose'}],
'Value to String'    :          [{name: 'to_string'}],
'Accumulate Field'   :          [{'data_type_loop': False}],
'Domain Size'        :          [{f: 'get', cache: True, ret: 'NODE', klass: 'Mesh',         parameters: {'component': 'MESH'}},
                                 {f: 'get', cache: True, ret: 'NODE', klass: 'Curve',        parameters: {'component': 'CURVE'}},
                                 {f: 'get', cache: True, ret: 'NODE', klass: 'Cloud',        parameters: {'component': 'POINTCLOUD'}},
                                 {f: 'get', cache: True, ret: 'NODE', klass: 'Instances',    parameters: {'component': 'INSTANCES'}},
                                 {f: 'get', cache: True, ret: 'NODE', klass: 'GreasePencil', parameters: {'component': 'GREASEPENCIL'}},
                                ],
'Attribute Statistic' :         [{}],
'Bake'               :          [{f: 'MANUAL'}],
'Blur Attribute'     :          [{name: 'blur'}],
'Bounding Box'       :          [{f: 'get'}],
'Capture Attribute'  :          [{f: 'MANUAL'}],
'Collection Info'    :          [{name: 'info', cache: True}],
'Convex Hull'        :          [{f: 'get'}],
'Corners of Edge'    :          [{f: 'STATIC'}],
'Corners of Face'    :          [{f: 'STATIC'}],
'Corners of Vertex'  :          [{f: 'STATIC'}],
'Arc'                :          [{f: 'C', name: 'Arc'}],
'Endpoint Selection' :          [{f: 'STATIC'}],
'Handle Type Selection' :       [{f: 'STATIC'}],
'Curve Length'       :          [{name: 'length'}],
'Curve of Point'     :          [{f: 'STATIC'}],
'Bézier Segment'     :          [{f: 'C', name: 'BezierSegment'}],
'Curve Circle'       :          [{f: 'C', name: 'Circle'}],
'Curve Line'         :          [{f: 'C', name: 'Line'}],
'Quadrilateral'      :          [{f: 'C'}],
'Quadratic Bézier'   :          [{f: 'C', name: 'QuadraticBezier'}],
'Set Handle Type'    :          [{},
                                 {name: 'set_left_handle_type',  parameters: {'mode': {'LEFT'}}},
                                 {name: 'set_right_handle_type', parameters: {'mode': {'RIGHT'}}},
                                 {name: 'set_both_handle_type',  parameters: {'mode': {'LEFT', 'RIGHT'}}},
                                ],
'Spiral'             :          [{f: 'C'}],
'Set Spline Type'    :          [{}],
'Star'               :          [{f: 'C'}],
'Curve to Mesh'      :          [{name: 'to_mesh'}],
'Curve to Points'    :          [{name: 'to_points'}],
'Curves to Grease Pencil' :     [{name: 'to_grease_pencil'}],
'Deform Curves on Surface' :    [{name: 'deform_on_surface'}],
'Delete Geometry'    :          [{}, {name: 'delete'}],
'Distribute Points in Grid' :   [{f: 'C', name: 'DistributeInGrid'}],
'Distribute Points in Volume' : [{name: 'distribute_points'}],
'Distribute Points on Faces' :  [{},
                                 {param_loop: 'distribute_method', prefix: 'distribute_points_on_faces_'},
                                 {name: 'distribute_points', klass: 'Face'},
                                 {param_loop: 'distribute_method', 'domain_value': 'FACE', prefix: 'distribute_points_'},
                                ],
'Dual Mesh'          :          [{name: 'dual'}],
'Duplicate Elements' :          [{name: 'duplicate'}],
'Edge Paths to Curves' :        [{}, {name: 'paths_to_curves', klass: 'Edge'}],
'Edge Paths to Selection' :     [{f: 'STATIC'}],
'Edges of Corner'    :          [{f: 'STATIC'}],
'Edges of Vertex'    :          [{f: 'STATIC'}],
'Edges to Face Groups' :        [{f: 'STATIC'}],
'Extrude Mesh'       :          [{name: 'extrude'}],
'Face of Corner'     :          [{f: 'STATIC'}],
'Evaluate at Index'  :          [{'data_type_loop': False}],
'Evaluate on Domain' :          [{'data_type_loop': False}],
'Fill Curve'         :          [{name: 'fill'}],
'Fillet Curve'       :          [{name: 'fillet'}],
'Flip Faces'         :          [{}, {name: 'flip', klass: 'Face'}],
'For Each Geometry Element Input'  : [{f: 'MANUAL'}],
'For Each Geometry Element Output' : [{f: 'MANUAL'}],
'Geometry to Instance' :        [{name: 'to_instance'},
                                 {f: 'C', name: 'FromGeometry'}
                                ],
'Get Named Grid'     :          [{},
                                 {parameters: {'data_type': 'FLOAT'},  name: 'named_float_grid' },
                                 {parameters: {'data_type': 'VECTOR'}, name: 'named_vector_grid'},
                                ],
'Dial Gizmo'         :          [{}],
'Linear Gizmo'       :          [{}],
'Transform Gizmo'    :          [{}],
'Grease Pencil to Curves' :     [{name: 'to_curves'}],
'Grid to Mesh'       :          [{name: 'to_mesh'}],
'Group'              :          [{f: 'MANUAL'}],
'Image Info'         :          [{f: 'get_out_loop', name: 'info'}],
'Image Texture'      :          [{f: 'C'}],
'Import OBJ'         :          [{f: 'C', name: 'ImportOBJ'}],
'Import PLY'         :          [{f: 'C', name: 'ImportPLY'}],
'Import STL'         :          [{f: 'C', name: 'ImportSTL'}],
'Index of Nearest'   :          [{f: 'STATIC'}],
'Index Switch'       :          [{f: 'STATIC'}],
'Active Camera'      :          [{f: 'C'}],
'Curve Handle Positions' :      [{f: 'STATIC'}],
'Curve Tilt'         :          [{f: 'STATIC'}],
'Is Edge Smooth'     :          [{f: 'STATIC'}],
'ID'                 :          [{f: 'STATIC'}],
'Image'              :          [{f: 'INIT'}],
'Index'              :          [{f: 'STATIC'}],
'Instance Rotation'  :          [{f: 'STATIC'}],
'Instance Scale'     :          [{f: 'STATIC'}],
'Material'           :          [{f: 'STATIC'}],
'Material Index'     :          [{f: 'STATIC'}],
'Edge Angle'         :          [{f: 'STATIC'}],
'Edge Neighbors'     :          [{f: 'STATIC'}],
'Edge Vertices'      :          [{f: 'STATIC'}],
'Face Area'          :          [{f: 'STATIC'}],
'Is Face Planar'     :          [{f: 'STATIC'}],
'Face Neighbors'     :          [{f: 'STATIC'}],
'Mesh Island'        :          [{f: 'STATIC'}],
'Vertex Neighbors'   :          [{f: 'STATIC'}],
'Named Attribute'    :          [{f: 'C', name: 'Named'}, {f: 'C', name: 'NamedAttribute'}, ],
'Named Layer Selection' :       [{f: 'STATIC'}],
'Normal'             :          [{f: 'STATIC'}],
'Position'           :          [{f: 'STATIC'}],
'Radius'             :          [{f: 'STATIC'}],
'Scene Time'         :          [{f: 'get', klass: 'Float', ret: 'NODE'},
                                 {f: 'get', name: 'seconds', klass: 'Float', ret: 'seconds'},
                                 {f: 'get', name: 'frame',   klass: 'Float', ret: 'frame'},
                                ],
'Is Face Smooth'     :          [{f: 'STATIC'}],
'Shortest Edge Paths' :         [{f: 'STATIC'}],
'Is Spline Cyclic'   :          [{f: 'STATIC'}],
'Spline Resolution'  :          [{f: 'STATIC'}],
'Curve Tangent'      :          [{f: 'STATIC'}],
'Instance on Points' :          [{name: 'instance_on_points'},
                                 {name: 'instance_on', klass:'Point'}, {name: 'instance_on', klass:'Cloud'},
                                ],
'Instance Transform' :          [{f: 'STATIC'}],
'Instances to Points' :         [{name: 'to_points'}],
'Interpolate Curves' :          [{f: 'C', name: 'Interpolate'}, {name: 'interpolate'}, {self_: 'Points'}],
'Is Viewport'        :          [{f: 'get', klass: 'Boolean'}],
'Join Geometry'      :          [{name: 'join'}, {f: 'C', name: 'Join'}],
'Material Selection' :          [{f: 'STATIC'}],
'Menu Switch'        :          [{f: 'MANUAL'}],
'Merge by Distance'  :          [{'mode_loop': False}, {name: 'merge'}],
'Merge Layers'       :          [{rename: {'merge_by_name': 'by_name', 'merge_by_id': 'by_id'}}],
'Mesh Boolean'       :          [{name: 'boolean'}, {f: 'C', name: 'Boolean'},
                                 {param_loop: 'operation'}, {f: 'C', param_loop: 'operation'},
                                ],
'Mesh Circle'        :          [{f: 'C', name: 'Circle'}],
'Cone'               :          [{f: 'C'}],
'Cube'               :          [{f: 'C'}],
'Cylinder'           :          [{f: 'C'}],
'Face Group Boundaries' :       [{f: 'STATIC'}],
'Grid'               :          [{f: 'C'}],
'Ico Sphere'         :          [{f: 'C'}],
'Mesh Line'          :          [{f: 'C', name: 'Line'}],
'Mesh to Curve'      :          [{name: 'to_curve'}],
'Mesh to Density Grid' :        [{name: 'to_density_grid'}],
'Mesh to Points'     :          [{name: 'to_points', 'mode_loop': False}, {param_loop: 'mode', suffix: '_to_points'}],
'Mesh to SDF Grid'   :          [{name: 'to_sdf_grid'}],
'Mesh to Volume'     :          [{name: 'to_volume'}],
'UV Sphere'          :          [{f: 'C', name: 'UVSphere'}],
'Object Info'        :          [{f: 'get', name: 'info', ret: 'NODE'}],
'Offset Corner in Face' :       [{f: 'STATIC'}],
'Offset Point in Curve' :       [{f: 'STATIC'}],
'Points'             :          [{f: 'C'}],
'Points of Curve'    :          [{f: 'STATIC'}],
'Points to Curves'   :          [{name: 'to_curves'}],
'Points to SDF Grid' :          [{name: 'to_sdf_grid'}],
'Points to Vertices' :          [{name: 'to_vertices'}],
'Points to Volume'   :          [{name: 'to_volume'}],
'Geometry Proximity' :          [{name: 'proximity'}, {param_loop: 'target_element', prefix: 'proximity_'}],
'Raycast'            :          [{ret: 'NODE'}, {param_loop: 'mapping', prefix: 'raycast_', ret: 'NODE'}],
'Realize Instances'  :          [{name: 'realize'}],
'Remove Named Attribute' :      [{},
                                 {name: 'remove_names', parameters: {'pattern_mode': 'WILDCARD'}}
                                ],
'Repeat Input'       :          [{f: 'MANUAL'}],
'Repeat Output'      :          [{f: 'MANUAL'}],
'Replace Material'   :          [{}],
'Resample Curve'     :          [{name: 'resample'}],
'Reverse Curve'      :          [{name: 'reverse'}],
'Rotate Instances'   :          [{name: 'rotate'}],
'SDF Grid Boolean'   :          [{name: 'grid_boolean'}, {param_loop: 'operation', 'prefix': 'sdf_'}],
'Sample Curve'       :          [{name: 'sample'}],
'Sample Grid'        :          [{}],
'Sample Grid Index'  :          [{}],
'Sample Index'       :          [{}],
'Sample Nearest'     :          [{}],
'Sample Nearest Surface' :      [{}],
'Sample UV Surface'  :          [{}],
'Scale Elements'     :          [{name: 'scale'}, {param_loop: 'scale_mode', prefix: 'scale_'}],
'Scale Instances'    :          [{name: 'scale'}],
'Self Object'        :          [{f: 'C', name: 'Self'}],
'Separate Components' :         [{f: 'get_out_loop'}],
'Separate Geometry'  :          [{name: 'separate'}],
'Set Handle Positions' :        [{'mode_loop': False}, {param_loop: 'mode', prefix: 'set_', suffix: '_handle_positions'}],
'Set Curve Normal'   :          [{name: 'set_normal'}],
'Set Curve Radius'   :          [{name: 'set_radius'}],
'Set Curve Tilt'     :          [{name: 'set_tilt'}],
'Set Geometry Name'  :          [{name: 'set_name'}],
'Set ID'             :          [{name: 'set_id'}],
'Set Instance Transform' :      [{name: 'set_transform'}],
'Set Material'       :          [{}],
'Set Material Index' :          [{}],
'Set Point Radius'   :          [{name: 'set_radius', domain: 'POINT'}],
'Set Position'       :          [{}],
'Set Shade Smooth'   :          [{}],
'Set Spline Cyclic'  :          [{}],
'Set Spline Resolution' :       [{}],
'Simulation Input'   :          [{f: 'MANUAL'}],
'Simulation Output'  :          [{f: 'MANUAL'}],
'Sort Elements'      :          [{name: 'sort'}],
'Spline Length'      :          [{f: 'STATIC'}],
'Spline Parameter'   :          [{f: 'STATIC'}],
'Split Edges'        :          [{}, {name: 'split', klass: 'Edge'}],
'Split to Instances' :          [{}],
'Store Named Attribute' :       [{}, {name: 'store'}, {name: 'store_uv', parameters: {'domain': 'CORNER', 'data_type': 'FLOAT2'}}],
'Store Named Grid'   :          [{}],
'Join Strings'       :          [{name: 'join'}, {f: 'C', name: 'Join'}],
'String to Curves'   :          [{name: 'to_curves'}],
'Subdivide Curve'    :          [{name: 'subdivide'}],
'Subdivide Mesh'     :          [{name: 'subdivide'}],
'Subdivision Surface' :         [{}],
'Switch'             :          [{f: 'MANUAL'}],
'3D Cursor'          :          [{f: 'STATIC'}],
'Active Element'     :          [{}],
'Face Set'           :          [{f: 'STATIC'}],
'Mouse Position'     :          [{f: 'STATIC'}],
'Selection'          :          [{f: 'STATIC'}],
'Set Face Set'       :          [{}],
'Set Selection'      :          [{}],
'Transform Geometry' :          [{only_enabled: False, 'mode_loop': False}, {param_loop: 'mode', name: 'transform'}],
'Translate Instances' :         [{name: 'translate'}],
'Triangulate'        :          [{}],
'Trim Curve'         :          [{name: 'trim'}],
'Pack UV Islands'    :          [{}, {domain: 'CORNER'}],
'UV Unwrap'          :          [{}, {domain: 'CORNER'}],
'Vertex of Corner'   :          [{f: 'STATIC'}],
'Viewer'             :          [{ret: None}],
'Viewport Transform' :          [{f: 'STATIC'}],
'Volume Cube'        :          [{f: 'C', name: 'Cube'}],
'Volume to Mesh'     :          [{name: 'to_mesh'}, {param_loop: 'resolution_mode', prefix: 'to_mesh_'}],
'Warning'            :          [{parameters: {'warning_type': 'ERROR'},   name: 'error'},
                                 {parameters: {'warning_type': 'WARNING'}, name: 'warning'},
                                 {parameters: {'warning_type': 'INFO'},    name: 'info'},
                                ],
'Frame'              :          [{f: 'MANUAL'}],
'Group Input'        :          [{f: 'MANUAL'}],
'Group Output'       :          [{f: 'MANUAL'}],
'Reroute'            :          [{f: 'MANUAL'}],
'Blackbody'          :          [{f: 'C'}],
'Clamp'              :          [{},
                                 {parameters: {'clamp_type': 'MINMAX'}, name: 'clamp_minmax'},
                                 {parameters: {'clamp_type': 'RANGE'},  name: 'clamp_range'},
                                ],
'Combine XYZ'        :          [{f: 'C', name: 'CombineXYZ'}],
'Float Curve'        :          [{}],
'Map Range'          :          [{},
                                 {param_loop: 'interpolation_type', prefix: 'map_range_', rename: {'smoothstep': 'smooth_step', 'smootherstep': 'smoother_step'}},
                                ],
'Math'               :          [{f: 'op', rename: {
                                        'minimum'      : 'min',
                                        'maximum'      : 'max',
                                        'logarithm'    : 'log',
                                        'absolute'     : 'abs',
                                        'exponent'     : 'exp',
                                        'sine'         : 'sin',
                                        'cosine'       : 'cos',
                                        'tangent'      : 'tan',
                                }},
                                {f: 'math', rename: {
                                        'minimum'      : 'min',
                                        'maximum'      : 'max',
                                        'logarithm'    : 'log',
                                        'absolute'     : 'abs',
                                        'exponent'     : 'exp',
                                        'sine'          : 'sin',
                                        'cosine'        : 'cos',
                                        'tangent'       : 'tan',
                                }},
                                ],
'Mix'                :          [{parameters: {'data_type': 'FLOAT', 'blend_type': 'MIX', 'factor_mode': 'UNIFORM', 'clamp_result': False}},
                                 {parameters: {'data_type': 'ROTATION', 'blend_type': 'MIX', 'factor_mode': 'UNIFORM', 'clamp_result': False}},
                                 {param_loop: 'factor_mode', prefix: 'mix_', parameters: {'data_type': 'VECTOR', 'blend_type': 'MIX', 'clamp_result': False}},
                                 {param_loop: 'blend_type',  prefix: 'mix_', parameters: {'data_type': 'RGBA', 'factor_mode': 'UNIFORM'}},
                                ],
'RGB Curves'         :          [{}],
'Separate XYZ'       :          [{f: 'get', name: 'xyz', cache: True, ret: 'TUPLE'},
                                 {f: 'get_out_loop'},
                                ],
'Brick Texture'      :          [{f: 'C', name: 'Brick'},      {f: 'cm', name: 'Brick',      klass: 'Texture'}],
'Checker Texture'    :          [{f: 'C', name: 'Checker'},    {f: 'cm', name: 'Checked',    klass: 'Texture'}],
'Gabor Texture'      :          [{f: 'C', name: 'Gabor'},      {f: 'cm', name: 'Gabor',      klass: 'Texture'}],
'Gradient Texture'   :          [{f: 'C', name: 'Gradient'},   {f: 'cm', name: 'Gradient',   klass: 'Texture'}],
'Magic Texture'      :          [{f: 'C', name: 'Magic'},      {f: 'cm', name: 'Magic',      klass: 'Texture'}],
'Noise Texture'      :          [{f: 'C', name: 'Noise'},      {f: 'cm', name: 'Noise',      klass: 'Texture'}],
'Voronoi Texture'    :          [{f: 'C', name: 'Voronoi'},    {f: 'cm', name: 'Voronoi',    klass: 'Texture'}],
'Wave Texture'       :          [{f: 'C', name: 'Wave'},       {f: 'cm', name: 'Wave',       klass: 'Texture'}],
'White Noise Texture' :         [{f: 'C', name: 'WhiteNoise'}, {f: 'cm', name: 'WhiteNoise', klass: 'Texture'}],
'Color Ramp'         :          [{f: 'MANUAL'}],
'Value'              :          [{f: 'INPUT'}],
'Vector Curves'      :          [{}],
'Vector Math'        :          [{f: 'op', rename: {
                                        'cross_product': 'cross',
                                        'dot_product'  : 'dot',
                                        'absolute'     : 'abs',
                                        'minimum'      : 'min',
                                        'maximum'      : 'max',
                                        'sine'         : 'sin',
                                        'cosine'       : 'cos',
                                        'tangent'      : 'tan',
                                }},
                                {f: 'math', rename: {
                                        'add'           : 'vadd',
                                        'subtract'      : 'vsubtract',
                                        'multiply'      : 'vmultiply',
                                        'divide'        : 'vdivide',
                                        'multiply_add'  : 'vmultiply_add',
                                        'cross_product' : 'cross',
                                        'dot_product'   : 'dot',
                                        'absolute'      : 'vabs',
                                        'minimum'       : 'vmin',
                                        'maximum'       : 'vmax',
                                        'floor'         : 'vfloor',
                                        'ceil'          : 'vceil',
                                        'fraction'      : 'vfraction',
                                        'wrap'          : 'vwrap',
                                        'snap'          : 'vsnap',
                                        'sine'          : 'vsin',
                                        'cosine'        : 'vcos',
                                        'tangent'       : 'vtan',
                                }},
                                ],
'Vector Rotate'      :          [{name: 'rotate'},
                                 {param_loop: 'rotation_type', prefix: 'rotate_'},
                                ],
}

GEONODES_PROPS = [
    {name: 'position', setter: 'Set Position', getter: 'Position',  in_socket: 'Position'},
    {name: 'offset',   setter: 'Set Position', getter:  None,       in_socket: 'Offset'},
    {name: 'id',       setter: 'Set ID',       getter: 'ID'},
    {name: 'material', setter: 'Set Material'},
    {name: 'name',     setter: 'Set Geometry Name'},
    {name: 'material_index', setter: 'Set Material Index', getter: 'Material Index'},

    {name: 'radius', setter: 'Set Point Radius', getter: 'Radius', klass: 'Cloud'},
    {name: 'radius', setter: 'Set Curve Radius', getter: 'Radius', klass: 'Curve'},

    {name: 'shade_smooth', setter: 'Set Shade Smooth', getter: {'Edge': 'Is Edge Smooth', 'Face': 'Is Face Smooth'}},
    {name: 'smooth',       setter: 'Set Shade Smooth', getter: {'Edge': 'Is Edge Smooth', 'Face': 'Is Face Smooth'}},

    {name: 'left_handle_position',  setter: 'Set Handle Positions', set_prm: {'mode': 'LEFT'},
        getter: 'Curve Handle Positions', get_sock: {'Relative': False}, out_socket: 'left'},
    {name: 'right_handle_position', setter: 'Set Handle Positions', set_prm: {'mode': 'RIGHT'},
        getter: 'Curve Handle Positions', get_sock: {'Relative': False}, out_socket: 'right'},
    {name: 'left_handle_offset',    setter: 'Set Handle Positions', set_prm: {'mode': 'LEFT'},  in_socket: 'Offset',
        getter: 'Curve Handle Positions', get_sock: {'Relative': True}, out_socket: 'left'},
    {name: 'right_handle_offset',   setter: 'Set Handle Positions', set_prm: {'mode': 'RIGHT'}, in_socket: 'Offset',
        getter: 'Curve Handle Positions', get_sock: {'Relative': True}, out_socket: 'right'},

    {name: 'handle_type',       setter: 'Set Handle Type', set_prm: {'mode': {'LEFT', 'RIGHT'}}},
    {name: 'left_handle_type',  setter: 'Set Handle Type', set_prm: {'mode': {'LEFT'}}},
    {name: 'right_handle_type', setter: 'Set Handle Type', set_prm: {'mode': {'RIGHT'}}},

    {name: 'transform', setter: 'Set Instance Transform', getter: 'Instance Transform'},

    {name: 'tilt',       setter: 'Set Curve Tilt', getter: 'Curve Tilt', klass: 'Curve'},
    {name: 'tilt',       setter: 'Set Curve Tilt', getter: 'Curve Tilt', klass: 'Spline'},
    {name: 'normal',     setter: 'Set Curve Normal', klass: 'Curve'},
    {name: 'normal',     setter: 'Set Curve Normal', klass: 'Spline'},
    {name: 'is_cyclic',  setter: 'Set Spline Cyclic', getter: 'Is Spline Cyclic', klass: 'Curve'},
    {name: 'is_cyclic',  setter: 'Set Spline Cyclic', getter: 'Is Spline Cyclic', klass: 'Spline'},
    {name: 'resolution', setter: 'Set Spline Resolution', getter: 'Spline Resolution', klass: 'Curve'},
    {name: 'resolution', setter: 'Set Spline Resolution', getter: 'Spline Resolution', klass: 'Spline'},
    {name: 'type',       setter: 'Set Spline Type', klass: 'Curve'},
    {name: 'type',       setter: 'Set Spline Type', klass: 'Spline'},
]

# =============================================================================================================================
# Generate

def generate(folder, tree_type='GeometryNodeTree'):

    print("Generate for tree_type", tree_type)

    tree_name = 'GENERATE'
    tree = bpy.data.node_groups.get(tree_name)
    tree = bpy.data.node_groups.new(tree_name, type=tree_type)
    tree.nodes.clear()

    path = Path(folder) / "generated"

    if tree_type == 'GeometryNodeTree':
        tree.is_modifier = True

        nodes = GEONODES
        props = GEONODES_PROPS
        static_nodes = 'nd'

    elif tree_type == 'ShaderNodeTree':
        path = Path(folder) / "gen_shader"

        static_nodes = 'snd'


    # ===== The result

    gen = {}

    # ===== Nodes as methods

    for node_name, impls in nodes.items():

        tree.nodes.clear()
        node_info = NodeInfo(tree, node_name)

        for impl in impls:
            node_info.source_code(gen, **impl)

    # ===== Nodes as properties

    for prop in props:
        tree.nodes.clear()
        NodeInfo.property_code(tree, gen, **prop)

    # ===== Nodes as static classes

    NodeInfo.gen_static_nodes(gen, tree_type=tree_type, verbose=False)

    # ===== Create the files

    print('='*100)

    imports = []
    for class_name, funcs in gen.items():

        print("Create file", class_name)
        module = class_name.lower()

        with open(path / f"{module}.py", 'w') as file:

            file.write("from .. socket_class import Socket\n")
            file.write("from .. treeclass import Node\n")
            file.write("from .. treeclass import utils\n")
            file.write("from .. scripterror import NodeError\n")
            file.write("\n")

            if class_name == 'gnmath':
                imports.append(f"from . import gnmath")

            elif class_name == 'static':
                file.write(f"class {static_nodes}:\n\n")

            else:
                file.write(f"class {class_name}(Socket):\n\n")
                imports.append(f"from .{module} import {class_name}")

            for name, code in funcs.items():
                file.write(code + "\n")

    # init file
    with open(path / "__init__.py", 'w') as file:
        file.write("\n".join(imports))




    print("Done")
