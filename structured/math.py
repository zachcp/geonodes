from geonodes.structured.scripterror import NodeError
from geonodes.structured.treeclass import Tree, Node
from geonodes.structured.floatclass import Float, Integer
from geonodes.structured.booleanclass import Boolean
from geonodes.structured.vectorclass import Vector

# =============================================================================================================================
# Boolean Math

def band(value, other):
    return Boolean(Node("Boolean Math", {0: value, 1: other}, operation='AND')._out)

def bor(value, other):
    return Boolean(Node("Boolean Math", {0: value, 1: other}, operation='OR')._out)

def bnot(value):
    return Boolean(Node("Boolean Math", {0: value}, operation='NOT')._out)

def nand(value, other):
    return Boolean(Node("Boolean Math", {0: value, 1: other}, operation='NAND')._out)

def nor(value, other):
    return Boolean(Node("Boolean Math", {0: value, 1: other}, operation='NOR')._out)

def xnor(value, other):
    return Boolean(Node("Boolean Math", {0: value, 1: other}, operation='XNOR')._out)

def xor(value, other):
    return Boolean(Node("Boolean Math", {0: value, 1: other}, operation='XOR')._out)

def imply(value, other):
    return Boolean(Node("Boolean Math", {0: value, 1: other}, operation='IMPLY')._out)

def nimply(value, other):
    return Boolean(Node("Boolean Math", {0: value, 1: other}, operation='NIMPLY')._out)


# =============================================================================================================================
# Float Math

def add(value, other, use_clamp=None):
    return Float(Node("Math", {0: value, 1: other}, use_clamp=use_clamp, operation='ADD')._out)

def subtract(value, other, use_clamp=None):
    return Float(Node("Math", {0: value, 1: other}, use_clamp=use_clamp, operation='SUBTRACT')._out)

def multiply(value, other, use_clamp=None):
    return Float(Node("Math", {0: value, 1: other}, use_clamp=use_clamp, operation='MULTIPLY')._out)

def divide(value, other, use_clamp=None):
    return Float(Node("Math", {0: value, 1: other}, use_clamp=use_clamp, operation='DIVIDE')._out)

def multiply_add(value, multiplier, addend, use_clamp=None):
    return Float(Node("Math", {0: value, 1: multiplier, 2: addend}, use_clamp=use_clamp, operation='MULTIPLY_ADD')._out)

def power(base, exponent, use_clamp=None):
    return Float(Node("Math", {0: base, 1: exponent}, use_clamp=use_clamp, operation='POWER')._out)

def log(value, base, use_clamp=None):
    return Float(Node("Math", {0: value, 1: other}, use_clamp=use_clamp, operation='LOGARITHM')._out)

def sqrt(value, other, use_clamp=None):
    return Float(Node("Math", {0: value, 1: base}, use_clamp=use_clamp, operation='SQRT')._out)

def inverse_sqrt(value, use_clamp=None):
    return Float(Node("Math", {0: value}, use_clamp=use_clamp, operation='INVERSE_SQRT')._out)

def abs(value, use_clamp=None):
    return Float(Node("Math", {0: value}, use_clamp=use_clamp, operation='ABSOLUTE')._out)

def exponent(value, use_clamp=None):
    return Float(Node("Math", {0: value}, use_clamp=use_clamp, operation='EXPONENT')._out)

def min(value, other, use_clamp=None):
    return Float(Node("Math", {0: value, 1: other}, use_clamp=use_clamp, operation='MINIMUM')._out)

def max(value, other, use_clamp=None):
    return Float(Node("Math", {0: value, 1: other}, use_clamp=use_clamp, operation='MAXIMUM')._out)

def less_than(value, threshold, use_clamp=None):
    return Float(Node("Math", {0: value, 1: threshold}, use_clamp=use_clamp, operation='LESS_THAN')._out)

def greater_than(value, threshold, use_clamp=None):
    return Float(Node("Math", {0: value, 1: threshold}, use_clamp=use_clamp, operation='GREATER_THAN')._out)

def sign(value, other, use_clamp=None):
    return Float(Node("Math", {0: value, 1: other}, use_clamp=use_clamp, operation='SIGN')._out)

def compare(value, other, epsilon=None, use_clamp=None):
    return Float(Node("Math", {0: value, 1: other, 2:epsilon}, use_clamp=use_clamp, operation='COMPARE')._out)

def smooth_min(value, other, distance=None, use_clamp=None):
    return Float(Node("Math", {0: value, 1: other, 2:distance}, use_clamp=use_clamp, operation='SMOOTH_MIN')._out)

def smooth_max(value, other, distance=None, use_clamp=None):
    return Float(Node("Math", {0: value, 1: other, 2: distance}, use_clamp=use_clamp, operation='SMOOTH_MAX')._out)

def round(value, use_clamp=None):
    return Float(Node("Math", {0: value}, use_clamp=use_clamp, operation='ROUND')._out)

def floor(value, use_clamp=None):
    return Float(Node("Math", {0: value}, use_clamp=use_clamp, operation='FLOOR')._out)

def ceil(value, use_clamp=None):
    return Float(Node("Math", {0: value}, use_clamp=use_clamp, operation='CEIL')._out)

def trunc(value, use_clamp=None):
    return Float(Node("Math", {0: value}, use_clamp=use_clamp, operation='TRUNC')._out)

def fract(value, use_clamp=None):
    return Float(Node("Math", {0: value}, use_clamp=use_clamp, operation='FRACT')._out)

def modulo(value, other, use_clamp=None):
    return Float(Node("Math", {0: value, 1: other}, use_clamp=use_clamp, operation='MODULO')._out)

def floored_modulo(value, other, use_clamp=None):
    return Float(Node("Math", {0: value, 1: other}, use_clamp=use_clamp, operation='FLOORED_MODULO')._out)

def wrap(value, max=None, min=None, use_clamp=None):
    return Float(Node("Math", {0: value, 1: max, 2: min}, use_clamp=use_clamp, operation='WRAP')._out)

def snap(value, increment=None, use_clamp=None):
    return Float(Node("Math", {0: value, 1: increment}, use_clamp=use_clamp, operation='SNAP')._out)

def pingpong(value, scale=None, use_clamp=None):
    return Float(Node("Math", {0: value, 1: scale}, use_clamp=use_clamp, operation='PINGPONG')._out)

def sin(value, use_clamp=None):
    return Float(Node("Math", {0: value}, use_clamp=use_clamp, operation='SINE')._out)

def cos(value, use_clamp=None):
    return Float(Node("Math", {0: value}, use_clamp=use_clamp, operation='COSINE')._out)

def tan(value, use_clamp=None):
    return Float(Node("Math", {0: value}, use_clamp=use_clamp, operation='TANGENT')._out)

def asin(value, use_clamp=None):
    return Float(Node("Math", {0: value}, use_clamp=use_clamp, operation='ARCSINE')._out)

def acos(value, use_clamp=None):
    return Float(Node("Math", {0: value}, use_clamp=use_clamp, operation='ARCCOSINE')._out)

def atan(value, use_clamp=None):
    return Float(Node("Math", {0: value}, use_clamp=use_clamp, operation='ARCTANGENT')._out)

def atan2(value, other, use_clamp=None):
    return Float(Node("Math", {0: value, 1: other}, use_clamp=use_clamp, operation='ARCTAN2')._out)

def sinh(value, use_clamp=None):
    return Float(Node("Math", {0: value}, use_clamp=use_clamp, operation='SINH')._out)

def cosh(value, use_clamp=None):
    return Float(Node("Math", {0: value}, use_clamp=use_clamp, operation='COSH')._out)

def tanh(value, use_clamp=None):
    return Float(Node("Math", {0: value}, use_clamp=use_clamp, operation='TANH')._out)

def radians(value, use_clamp=None):
    return Float(Node("Math", {0: value}, use_clamp=use_clamp, operation='RADIANS')._out)

def degrees(value, use_clamp=None):
    return Float(Node("Math", {0: value}, use_clamp=use_clamp, operation='DEGREES')._out)

# =============================================================================================================================
# Vector Math

def vadd(value, other):
    return Vector(Node("Vector Math", {0: value, 1: other}, operation='ADD')._out)

def vsubtract(value, other):
    return Vector(Node("Vector Math", {0: value, 1: other}, operation='SUBTRACT')._out)

def vmultiply(value, other):
    return Vector(Node("Vector Math", {0: value, 1: other}, operation='MULTIPLY')._out)

def vdivide(value, other):
    return Vector(Node("Vector Math", {0: value, 1: other}, operation='DIVIDE')._out)

def vmultiply_add(value, maultiplie, addend):
    return Vector(Node("Vector Math", {0: value, 1: multiplier, 2: addend}, operation='MULTIPLY_ADD')._out)

def cross_product(value, other):
    return Vector(Node("Vector Math", {0: value, 1: other}, operation='CROSS_PRODUCT')._out)

def project(value, other):
    return Vector(Node("Vector Math", {0: value, 1: other}, operation='PROJECT')._out)

def reflect(value, other):
    return Vector(Node("Vector Math", {0: value, 1: other}, operation='REFLECT')._out)

def refract(value, other, ior=None):
    return Vector(Node("Vector Math", {0: value, 1: other, 'IOR': ior}, operation='REFRACT')._out)

def faceforward(value, incident=None, reference=None):
    return Vector(Node("Vector Math", {0: value, 1: incident, 2: reference}, operation='FACEFORWARD')._out)

def dot_product(value, other):
    return Float(Node("Vector Math", {0: value, 1: other}, operation='DOT_PRODUCT')._out)

def distance(value, other):
    return Float(Node("Vector Math", {0: value, 1: other}, operation='DISTANCE')._out)

def length(value):
    return Float(Node("Vector Math", {0: value}, operation='LENGTH')._out)

def scale(value, scale):
    return Vector(Node("Vector Math", {0: value, 'Scale': scale}, operation='SCALE')._out)

def normalize(value):
    return Vector(Node("Vector Math", {0: value}, operation='NORMALIZE')._out)

def babs(value):
    return Vector(Node("Vector Math", {0: value}, operation='ABSOLUTE')._out)

def vmin(value, other):
    return Vector(Node("Vector Math", {0: value, 1: other}, operation='MINIMUM')._out)

def vmax(value, other):
    return Vector(Node("Vector Math", {0: value, 1: other}, operation='MAXIMUM')._out)

def vfloor(value):
    return Vector(Node("Vector Math", {0: value}, operation='FLOOR')._out)

def vceil(value):
    return Vector(Node("Vector Math", {0: value}, operation='CEIL')._out)

def vfraction(value):
    return Vector(Node("Vector Math", {0: value}, operation='FRACTION')._out)

def vmodulo(value, other):
    return Vector(Node("Vector Math", {0: value, 1: other}, operation='MODULO')._out)

def vwrap(value, max=None, min=None):
    return Vector(Node("Vector Math", {0: value, 'Max': max, 'Min': min}, operation='WRAP')._out)

def vsnap(value, increment):
    return Vector(Node("Vector Math", {0: value, 'Increment': increment}, operation='SNAP')._out)

def vsin(value):
    return Vector(Node("Vector Math", {0: value}, operation='SINE')._out)

def vcos(value):
    return Vector(Node("Vector Math", {0: value}, operation='COSINE')._out)

def vtan(value):
    return Vector(Node("Vector Math", {0: value}, operation='TANGENT')._out)
