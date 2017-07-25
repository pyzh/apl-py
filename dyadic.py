"""
    dyadic APL functions

    WIP - This module supports mixed scalar/vector expressions.  Arrays are not supported.

    The base functions are private Python functions.  They take two and return one Python number.

    Here a Python number is typically float:  complex numbers are not supported.

    Some functions may raise the APL 'DOMAIN ERROR' but none should raise a Python exception.

    WIP - Many base functions still to implement.
"""

import operator
import math
import random
import mpmath

from system_vars import confirm_bool, confirm_int, equalCT, integerCT, indexOrigin

from apl_quantity import ss2s, ss2v, sv_rho, vv_comma, vv2v, vv2s, sv2vr, sv2vl, sv_transpose, ce2v
from apl_error import apl_error

# ------------------------------

def     _add (A,B):
    """
    A plus B
    """
    return operator.add(A,B)

# --------------

def     _subtract (A,B):
    """
    A minus B
    """
    return operator.sub(A,B)

# --------------

def     _multiply (A,B):
    """
    A times B
    """
    return operator.mul(A,B)

# --------------

def     _divide (A,B):
    """
    A divided by B - may raise DOMAIN ERROR
    """
    try:
        return operator.truediv(A,B)
    except:
        if equalCT(A,0) and equalCT(B,0):   return 1

        apl_error("DOMAIN ERROR")

# --------------

def     _maximum (A,B):
    """
    A maximum B
    """
    return max(A,B)

# --------------

def     _minimum (A,B):
    """
    A minimum B
    """
    return min(A,B)

# --------------

def     _residue (A,B):
    """
    B modulo A with comparison tolerance
    """
    if type(A) is int:
        if A == 0:          return B
    else:
        if equalCT(A,0):    return B

    if type(integerCT(operator.truediv(B,A))) is int:
        return 0

    result = math.fmod(B,A)

    if result < 0:
        if A > 0:       result += A
    elif result > 0:
        if A < 0:       result += A
    else:
        result = 0.0

    if type(A) is int and type(B) is int:
        return int(result)
    else:
        return result

# ------------------------------

def     _exp (A,B):
    """
    A to the power B - may raise DOMAIN ERROR
    """
    try:
        return math.pow(A,B)
    except ValueError:
        apl_error("DOMAIN ERROR")

# --------------

def     _log (A,B):
    """
    log to base A of B - may raise DOMAIN ERROR
    """
    try:
        if A == 10: return math.log10(B)
        # Python 3.3 and later # if A == 2:  return math.log2(B)

        return math.log(B,A)

    except ValueError:
        if equalCT(A,B):  return 1.0
        if equalCT(A,0):  return 0.0
        if equalCT(B,1):  return 0.0

    except ZeroDivisionError:
        if equalCT(A,B):  return 1.0

    apl_error("DOMAIN ERROR")

# --------------

def     _deal (A,B):
    """
    random selection of A numbers from the range [1,B] without replacement - may raise DOMAIN ERROR
    """

    A = confirm_int(A)
    B = confirm_int(B)

    try:
        return random.sample(range(1,B+1),A)
    except ValueError:
        apl_error("DOMAIN ERROR")

# --------------

def     _combinations (A,B):
    """
    number of combinations of size A from a population of size B - may raise DOMAIN ERROR

    for floating point numbers this is binomial(B,A)

    rules for negative integers and floating point are interesting
    """

    try:
        if type(A) is int and type(B) is int:
            return int(mpmath.binomial(B,A))
        else:
            return float(mpmath.binomial(B,A))
    except ValueError:
        apl_error("DOMAIN ERROR")

# ------------------------------

_trigonometric_functions = (
    None,               # -12
    None,
    None,
    None,
    None,               # -8
    math.atanh,
    math.acosh,
    math.asinh,
    lambda x: math.sqrt(x*x-1), # -4
    math.atan,
    math.acos,
    math.asin,
    lambda x: math.sqrt(1-x*x), # 0
    math.sin,
    math.cos,
    math.tan,
    lambda x: math.sqrt(x*x+1), # +4
    math.sinh,
    math.cosh,
    math.tanh,
    None,               # +8
    None,
    None,
    None,
    None,               # +12
)

# --------------

def     _trigonometric (A,B):
    """
    A(B) where A is a trignometic function and B is an angle in Radians

    A is valid in the range [-12,+12].  The following are implemented:

    ¯7  atanh(B)
    ¯6  acosh(B)
    ¯5  asinh(B)
    ¯4  sqrt(B**2-1)
    ¯3  atan(B)
    ¯2  acos(B)
    ¯1  asin(B)
     0  sqrt(1-B**2)
     1  sin(B)
     2  cos(B)
     3  tan(B)
     4  sqrt(B**2+1)
     5  sinh(B)
     6  cosh(B)
     7  tanh(B)
    """
    A = confirm_int(A)

    if A <= -12 or A >= 12:
        apl_error("DOMAIN ERROR")

    function = _trigonometric_functions[A+12]
    if function is None:
        return to_be_implemented(A,B)

    try:
        return function(B)
    except ValueError:
        apl_error("DOMAIN ERROR")


# ------------------------------

def     _highest_common_factor (A,B):
    """
    Highest Common Factor by the Euclid method

    Note: math.gcd() is Python 3.5 and later
    """
    if B == 0:
        return abs(A)

    return _highest_common_factor(B, A % B)

# --------------

def     _or_gcd (A,B):
    """
    A or B (Boolean); GCD(A,B) (otherwise)
    """
    try:
        return int(confirm_bool(A) + confirm_bool(B) != 0)
    except:
        return _highest_common_factor(A,B)

# --------------

def     _and_lcm (A,B):
    """
    A and B (Boolean); LCM(A,B) (otherwise)
    """
    try:
        return int(confirm_bool(A) + confirm_bool(B) == 2)
    except:
        return A * B / _highest_common_factor(A,B)

# --------------

def     _nor (A,B):
    """
    A nor B - may raise DOMAIN ERROR
    """
    return int(confirm_bool(A) + confirm_bool(B) == 0)

# --------------

def     _nand (A,B):
    """
    A nand B - may raise DOMAIN ERROR
    """
    return int(confirm_bool(A) + confirm_bool(B) != 2)

# ------------------------------

def     _lt (A,B):
    """
    A < B with comparison tolerance
    """
    if type(A) is int and type(B) is int:
        return int(operator.lt(A,B))

    if equalCT(A,B):
        return 0

    return int(operator.lt(A,B))

# --------------

def     _le (A,B):
    """
    A <= B
    """
    if type(A) is int and type(B) is int:
        return int(operator.le(A,B))

    if equalCT(A,B):
        return 1

    return int(operator.le(A,B))

# --------------

def     _eq (A,B):
    """
    A == B with comparison tolerance
    """
    if type(A) is int and type(B) is int:
        return int(operator.eq(A,B))

    return int(equalCT(A,B))

# --------------

def     _ge (A,B):
    """
    A >= B with comparison tolerance
    """
    if type(A) is int and type(B) is int:
        return int(operator.ge(A,B))

    if equalCT(A,B):
        return 1

    return int(operator.ge(A,B))

# --------------

def     _gt (A,B):
    """
    A > B with comparison tolerance
    """
    if type(A) is int and type(B) is int:
        return int(operator.gt(A,B))

    if equalCT(A,B):
        return 0

    return int(operator.gt(A,B))

# --------------

def     _ne (A,B):
    """
    A != B with comparison tolerance
    """
    if type(A) is int and type(B) is int:
        return int(operator.ne(A,B))

    return int(not equalCT(A,B))

# ------------------------------

def     _without (A,B):
    """
    remove (elements of B) from (list) A
    """
    A = list(A)

    for X in B:
        try:
            while True:
                A.remove(X)
        except ValueError:
            pass

    return A

# --------------

def     _index (A,B):
    """
    index(es) of (elements of) B in (list) A
    """
    V = []
    IO = indexOrigin()

    A = list(A)

    for X in B:
        try:
            V.append(A.index(X) + IO)
        except ValueError:
            V.append(len(A) + IO)

    return V

# --------------

def     _take (A,B):
    """
    take A elements from B
    """
    A = confirm_int(A)
    if type(B) != str:  B = list(B)
    LB = len(B)

    if A < 0:
        if (0 > LB + A):
            if type(B) == str:
                return (' ' * (0 - (LB + A))) + B
            else:
                return ([0] * (0 - (LB + A))) + B
        else:
            return B[LB + A:]
    else:
        if (0 > LB - A):
            if type(B) == str:
                return B + (' ' * (0 - (LB - A)))
            else:
                return B + ([0] * (0 - (LB - A)))
        else:
            return B[:A]

# --------------

def     _drop (A,B):
    """
    drop A elements from B
    """
    A = confirm_int(A)
    if type(B) != str:  B = list(B)
    LB = len(B)

    if A < 0:
        if (0 > LB + A):
            return ''
        else:
            return B[:LB + A]
    else:
        return B[A:]

# --------------

def     _rotatelast (A,B):
    """
    rotate (vector) B by A elements
    """
    A = confirm_int(A) % len(B)

    return B[A:] + B[:A]

# --------------

def     _rotatefirst (A,B):
    """
    rotate (vector) B by A elements
    """
    A = confirm_int(A) % len(B)

    return B[A:] + B[:A]

# ------------------------------

def     _reshape (A,B):
    """
    reshape (list) B to have length A by replication and/or truncation
    """
    A = confirm_int(A)
    B = list(B)

    length = len(B)

    tail = A % length

    count = int((A - tail) / length)

    return B * count + B [:tail]

# ------------------------------

def     _concatenation (A,B):
    """
    concatenate (list) B onto the end of (list) A
    """
    return A + B

# ------------------------------

def     _union (A,B):
    """
    return union of B with A

    NB  only good for homogeneous operands
    """
    V = list(A)

    for X in B:
        if X not in A:
            V.append(X)

    return V

# ------------------------------

def     _intersection (A,B):
    """
    return intersection of of B with A

    NB  only good for homogeneous operands
    """
    V = []

    for X in A:
        if X in B:
            V.append(X)

    return V

# ------------------------------

def     _transpose (A,B):
    """
    transpose B about A
    """
    return B

# ------------------------------

def     _compress (A,B,pad):
    """
    compress/replicate B using A as the template
    """

    R = []

    I = B.__iter__()

    try:
        for X in A:
            X = confirm_int(X)

            V = I.__next__()

            if X > 0:
                for Y in range(X):
                    R.append(V)
            elif X < 0:
                for Y in range(-X):
                    R.append(pad)
            else:
                pass

    except StopIteration:
        if len(B) != 0:
            apl_error ("LENGTH ERROR")

    try:
        V = I.__next__()
    except StopIteration:
        pass
    else:
        apl_error ("LENGTH ERROR")

    return R

# ------------------------------

def     _expand (A,B,pad):
    """
    expand B using A as the template
    """
    R = []

    I = B.__iter__()

    try:
        for X in A:
            X = confirm_int(X)

            if X > 0:
                V = I.__next__()
                for Y in range(X):
                    R.append(V)
            elif X < 0:
                for Y in range(-X):
                    R.append(pad)
            else:
                R.append(pad)

    except StopIteration:
        apl_error ("LENGTH ERROR")

    try:
        V = I.__next__()
    except StopIteration:
        pass
    else:
        apl_error ("LENGTH ERROR")

    return R

# ------------------------------

def     to_be_implemented (A,B):
    """
    placeholder for functions not yet implemented

    raises FUNCTION NOT YET IMPLEMENTED
    """
    apl_error("FUNCTION NOT YET IMPLEMENTED")

# ------------------------------

_dyadic_functions = {
    # Mathematical
    '+':        lambda A,B: ss2s(_add,A,B,True),
    '-':        lambda A,B: ss2s(_subtract,A,B,True),
    '×':        lambda A,B: ss2s(_multiply,A,B,True),
    '÷':        lambda A,B: ss2s(_divide,A,B,True),
    '⌈':        lambda A,B: ss2s(_maximum,A,B,True),
    '⌊':        lambda A,B: ss2s(_minimum,A,B,True),
    '|':        lambda A,B: ss2s(_residue,A,B,True),

    # Algebraic
    '*':        lambda A,B: ss2s(_exp,A,B,True),
    '⍟':        lambda A,B: ss2s(_log,A,B,True),
    '?':        lambda A,B: ss2v(_deal,A,B),
    '!':        lambda A,B: ss2s(_combinations,A,B,True),
    '⌹':        to_be_implemented,      # matrix divide

    # Trigonometric
    '○':        lambda A,B: ss2s(_trigonometric,A,B,True),

    # Logical
    '∨':        lambda A,B: ss2s(_or_gcd,A,B,True),
    '∧':        lambda A,B: ss2s(_and_lcm,A,B,True),
    '⍱':        lambda A,B: ss2s(_nor,A,B,True),
    '⍲':        lambda A,B: ss2s(_nand,A,B,True),

    # Comparison
    '<':        lambda A,B: ss2s(_lt,A,B,True),
    '≤':        lambda A,B: ss2s(_le,A,B,True),
    '=':        lambda A,B: ss2s(_eq,A,B,False),
    '≥':        lambda A,B: ss2s(_ge,A,B,True),
    '>':        lambda A,B: ss2s(_gt,A,B,True),
    '≠':        lambda A,B: ss2s(_ne,A,B,False),
    '≡':        to_be_implemented,      # match (return 0/1 irrespective of rank etc)
    '≢':        to_be_implemented,      # not match

    # Structural (aka manipulative)
    '⍴':        lambda A,B: sv_rho(_reshape,A,B),
    ',':        lambda A,B: vv_comma(_concatenation,A,B),
    '⍪':        lambda A,B: vv_comma(_concatenation,A,B),
    '⌽':        lambda A,B: sv2vr(_rotatelast,A,B),
    '⊖':        lambda A,B: sv2vr(_rotatefirst,A,B),
    '⍉':        lambda A,B: sv_transpose(_transpose,A,B),
    '⊃':        to_be_implemented,      # pick (disclose) = picks from an array (?!?)
    '⊂':        to_be_implemented,      # partitioned enclose - creates an array of vectors (?!?)

    # Selection and Set Operations
    '~':        lambda A,B: vv2v(_without,A,B),
    '⍳':        lambda A,B: vv2s(_index,A,B),
    '↑':        lambda A,B: sv2vl(_take,A,B),
    '↓':        lambda A,B: sv2vl(_drop,A,B),
    '∪':        lambda A,B: vv2v(_union,A,B),
    '∩':        lambda A,B: vv2v(_intersection,A,B),
    '/':        lambda A,B: ce2v(_compress,A,B),
    '⌿':        lambda A,B: ce2v(_compress,A,B),
    '\\':       lambda A,B: ce2v(_expand,A,B),
    '⍀':        lambda A,B: ce2v(_expand,A,B),
    '⌷':        to_be_implemented,      # index
    '⊣':        to_be_implemented,      # left (discard right hand argument)
    '⊢':        to_be_implemented,      # right (discard left hand argument)

# Search
    '∊':        to_be_implemented,      # membership - is A in B (also characters) - returns a boolean
    '⍷':        to_be_implemented,      # find (look for a substring)

# Sorting
    '⍋':        to_be_implemented,      # Sort ascending with specified collating sequence
    '⍒':        to_be_implemented,      # Sort descending with specified collating sequence

# Encode/decode
    '⊤':        to_be_implemented,      # (encode) Convert to a new number system
    '⊥':        to_be_implemented,      # (decode) Convert back to units

# Formatting
    '⍕':        to_be_implemented,      # Format data for display
    '⍎':        to_be_implemented,      # dyadic execute
    '⍺':        to_be_implemented,      # Use picture to format data for display
};

# ------------------------------

def     dyadic_function (symbol):
    """
    return the dyadic function given its APL symbol

    raises INVALID TOKEN if the symbol is not recognised
    """
    try:
        return _dyadic_functions[symbol[0]]
    except KeyError:
        apl_error("INVALID TOKEN", symbol)

# EOF
