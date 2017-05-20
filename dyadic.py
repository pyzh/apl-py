"""
    dyadic APL functions

    WIP - limited set

    WIP - extended to handle APL scalars and vectors
"""

import operator
import math
import random
import mpmath

from system_vars import confirm_bool, confirm_int, equalCT, integerCT

from apl_quantity import dyadic2scalar, dyadic2vector
from apl_error import apl_error

# --------------

trigonometric_functions = (
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

def     add (A,B):
    """
    A plus B

    scalar arguments only
    """
    return operator.add(A,B)

def     subtract (A,B):
    """
    A minus B

    scalar arguments only
    """
    return operator.sub(A,B)

def     multiply (A,B):
    """
    A multiplied by B

    scalar arguments only
    """
    return operator.mul(A,B)

def     divide (A,B):
    """
    A divided by B

    scalar arguments only

    throws RANGE ERROR (B == 0)
    """
    try:
        return operator.truediv(A,B)
    except:
        apl_error("DOMAIN ERROR")

def     maximum (A,B):
    """
    A maximum B

    scalar arguments only
    """
    return max(A,B)

def     minimum (A,B):
    """
    A minimum B

    scalar arguments only
    """
    return min(A,B)

def     exp (A,B):
    """
    A to the power B

    scalar arguments only
    """
    try:
        return math.pow(A,B)
    except ValueError:
        apl_error("DOMAIN ERROR")

def     log (A,B):
    """
    log to base A of B

    scalar arguments only
    """
    try:
        if A == 10: return math.log10(B)
        # Python 3.3 and later # if A == 2:  return math.log2(B)
        if A == 0:  return 0.0

        return math.log(B,A)
    except ValueError:
        apl_error("DOMAIN ERROR")

def     residue (A,B):
    """
    B modulo A with comparison tolerance

    scalar arguments only
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

def     deal (A,B):
    """
    random selection of A numbers from the range [1,B] without replacement

    scalar arguments only
    """

    A = confirm_int(A)
    B = confirm_int(B)

    try:
        return random.sample(range(1,B+1),A)
    except ValueError:
        apl_error("DOMAIN ERROR")

def     combinations (A,B):
    """
    number of combinations of size A from a population of size B

    for floating point numbers this is binomial(B,A)

    rules for negative integers and floating point are interesting

    scalar arguments only
    """

    try:
        if type(A) is int and type(B) is int:
            return int(mpmath.binomial(B,A))
        else:
            return float(mpmath.binomial(B,A))
    except ValueError:
        apl_error("DOMAIN ERROR")

def     trigonometric (A,B):
    """
    A plus B

    scalar arguments only
    """
    if type(A) is int:
        if abs(A) <= 12:
            function = trigonometric_functions[A+12]
            if function is None:
                return to_be_implemented (A,B)
            else:
                return function(B)

    apl_error("DOMAIN ERROR")

# ------------------------------

def     _highest_common_factor (A,B):
    """
    Highest Common Factor by the Euclid method

    scalar argument only

    Note: math.gcd() is Python 3.5 and later
    """
    if B == 0:
        return abs(A)

    return _highest_common_factor(B, A % B)

def     or_gcd (A,B):
    """
    A or B (Boolean); GCD(A,B) otherwise

    scalar arguments only
    """
    try:
        return int(confirm_bool(A) + confirm_bool(B) != 0)
    except:
        return _highest_common_factor(A,B)

def     and_lcm (A,B):
    """
    A and B (Boolean); LCM(A,B) otherwise

    scalar arguments only
    """
    try:
        return int(confirm_bool(A) + confirm_bool(B) == 2)
    except:
        return A * B / _highest_common_factor(A,B)

def     nor (A,B):
    """
    A nor B

    scalar arguments only

    throws DOMAIN ERROR (B is not 0 or 1)
    """
    return int(confirm_bool(A) + confirm_bool(B) == 0)

def     nand (A,B):
    """
    A nand B

    scalar arguments only

    throws DOMAIN ERROR (B is not 0 or 1)
    """
    return int(confirm_bool(A) + confirm_bool(B) != 2)

# ------------------------------

def     lt (A,B):
    """
    A < B with comparison tolerance

    scalar arguments only
    """
    if type(A) is int and type(B) is int:
        return int(operator.lt(A,B))

    if equalCT(A,B):
        return 0

    return int(operator.lt(A,B))

def     le (A,B):
    """
    A <= B

    scalar arguments only
    """
    if type(A) is int and type(B) is int:
        return int(operator.le(A,B))

    if equalCT(A,B):
        return 1

    return int(operator.le(A,B))

def     eq (A,B):
    """
    A == B with comparison tolerance

    scalar arguments only
    """
    if type(A) is int and type(B) is int:
        return int(operator.eq(A,B))

    return int(equalCT(A,B))

def     ge (A,B):
    """
    A >= B with comparison tolerance

    scalar arguments only
    """
    if type(A) is int and type(B) is int:
        return int(operator.ge(A,B))

    if equalCT(A,B):
        return 1

    return int(operator.ge(A,B))

def     gt (A,B):
    """
    A > B with comparison tolerance

    scalar arguments only
    """
    if type(A) is int and type(B) is int:
        return int(operator.gt(A,B))

    if equalCT(A,B):
        return 0

    return int(operator.gt(A,B))

def     ne (A,B):
    """
    A != B with comparison tolerance

    scalar arguments only
    """
    if type(A) is int and type(B) is int:
        return int(operator.ne(A,B))

    return int(not equalCT(A,B))

# ------------------------------

def     to_be_implemented (A,B):
    """
    placeholder for functions not yet implemented

    throws FUNCTION NOT YET IMPLEMENTED
    """
    apl_error("FUNCTION NOT YET IMPLEMENTED")

# ------------------------------

dyadic_functions = {
    # Mathematical
    '+':        lambda A,B: dyadic2scalar(add,A,B),
    '-':        lambda A,B: dyadic2scalar(subtract,A,B),
    '×':        lambda A,B: dyadic2scalar(multiply,A,B),
    '÷':        lambda A,B: dyadic2scalar(divide,A,B),
    '⌈':        lambda A,B: dyadic2scalar(maximum,A,B),
    '⌊':        lambda A,B: dyadic2scalar(minimum,A,B),
    '|':        lambda A,B: dyadic2scalar(residue,A,B),

    # Algebraic
    '*':        lambda A,B: dyadic2scalar(exp,A,B),
    '⍟':        lambda A,B: dyadic2scalar(log,A,B),
    '?':        lambda A,B: dyadic2vector(deal,A,B),
    '!':        lambda A,B: dyadic2scalar(combinations,A,B),
    '○':        lambda A,B: dyadic2scalar(trigonometric,A,B),
    '⌹':        to_be_implemented,      # matrix divide

    # Logical
    '∨':        lambda A,B: dyadic2scalar(or_gcd,A,B),
    '∧':        lambda A,B: dyadic2scalar(and_lcm,A,B),
    '⍱':        lambda A,B: dyadic2scalar(nor,A,B),
    '⍲':        lambda A,B: dyadic2scalar(nand,A,B),

    # Comparison
    '<':        lambda A,B: dyadic2scalar(lt,A,B),
    '≤':        lambda A,B: dyadic2scalar(le,A,B),
    '=':        lambda A,B: dyadic2scalar(eq,A,B),
    '≥':        lambda A,B: dyadic2scalar(ge,A,B),
    '>':        lambda A,B: dyadic2scalar(gt,A,B),
    '≠':        lambda A,B: dyadic2scalar(ne,A,B),
    '≡':        to_be_implemented,      # match (return 0/1 irrespective of rank etc)

# Structural (aka manipulative)
    '⍴':        to_be_implemented,      # (rho) reshape
    ',':        to_be_implemented,      # (comma) concatenation
    '⍪':        to_be_implemented,      #
    '⌽':        to_be_implemented,      # rotation, last axis
    '⊖':        to_be_implemented,      # rotation, first axis
    '⍉':        to_be_implemented,      # transpose
    '⊂':        to_be_implemented,      # (enclose) - creates an array of vectors (?!?)
    '⊃':        to_be_implemented,      # (disclose) = picks from an array (?!?)

# Selection and Set Operations
    '\\':       to_be_implemented,      # expansion
    '/':        to_be_implemented,      # compression
    '↑':        to_be_implemented,      # take
    '↓':        to_be_implemented,      # drop
    '⌷':        to_be_implemented,      # index
    '~':        to_be_implemented,      # without - removes items
    '⌿':        to_be_implemented,      #
    '⍀':        to_be_implemented,      #
    '∪':        to_be_implemented,      #
    '∩':        to_be_implemented,      #
    '⊣':        to_be_implemented,      #
    '⊢':        to_be_implemented,      #

# Search
    '⍳':        to_be_implemented,      # index of B in A
    '∈':        to_be_implemented,      # membership ... same as ?
    '∊':        to_be_implemented,      # membership - is A in B (also characters) - return a boolean
    '⍷':        to_be_implemented,      # find (look for a substring)

# Sorting
    '⍋':        to_be_implemented,      # Sort ascending with specified collating sequence
    '⍒':        to_be_implemented,      # Sort descending with specified collating sequence

# Encode/decode
    '⊤':        to_be_implemented,      # (encode) Convert to a new number system
    '⊥':        to_be_implemented,      # (decode) Convert back to units

# Formatting
    '⍕':        to_be_implemented,      # Format data for display
    '⍺':        to_be_implemented,      # Use picture to format data for display
};

# ------------------------------

def     dyadic_function (symbol):
    """
    return the dyadic function given its APL symbol

    throws INVALID TOKEN if the symbol is not recognised
    """
    try:
        return dyadic_functions[symbol[0]]
    except KeyError:
        apl_error("INVALID TOKEN", symbol)

# EOF
