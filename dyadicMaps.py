"""
    map functions for dyadic APL functions

    UNDER DEVELOPMENT

    This module contains functions that map mathematical scalar functions over
    vectors and higher order arrays with the help of iterators functions.  It
    also contains functions that map non-mathematical vector functions.

    The external view is a map function but internally the functions delegate.
    Their task is a validate parameters and handle degenerate cases.

    WIP - the implementation of lazy evaluation means all functions in this
    module are under review.
"""

from aplQuantity import aplQuantity
from aplError import aplError

# ------------------------------
# OLD IMPLEMENTATIONS TO BE REPLACED
# ------------------------------

def     ss2s(Fn, A, B, numbersOnly):
    """
    evaluate a dyadic function that, given scalar arguments, returns a scalar
    """
    if numbersOnly:
        A.noStringConfirm()
        B.noStringConfirm()

    dims = tuple(filter(lambda X: X is not None, (A.dimension(), B.dimension())))
    case = len(dims)

    if case == 0:
        return aplQuantity(Fn(A.python(), B.python()), None)

    if case == 2:
        if dims[0] != dims[1]:
            aplError("LENGTH ERROR")

    return aplQuantity(map(Fn, A, B), dims[0])

# ------------------------------

def     ss2v(Fn, A, B):
    """
    evaluate a numeric dyadic function that, given scalar arguments, returns a vector
    """
    return aplQuantity(Fn(A.scalarToPy(), B.scalarToPy()), A)

# ------------------------------

def     vv2v(Fn, A, B):
    """
    evaluate a dyadic function that returns a vector
    """
    case = A.isString() + B.isString()

    if case == 1:
        return A

    Rpy = Fn(A.vectorToPy(), B.vectorToPy())

    return aplQuantity(Rpy, len(Rpy), case == 2)

# ------------------------------

def     vv2s(Fn, A, B):
    """
    evaluate a dyadic function that returns a vector if B is a vector but a scalar if B is scalar
    """
    case = A.isString() + B.isString()

    Rpy = Fn(A.vectorToPy(), B.vectorToPy(), case == 1)

    if B.isScalar():
        return aplQuantity(Rpy[0], None)

    if B.isVector():
        return aplQuantity(Rpy, B.dimension())

    aplError("RANK ERROR")

# ------------------------------

def     sv_rho(Fn, A, B):
    """
    evaluate a dyadic function that may take a scalar/vector and a vector and return a vector

    well, this is for ⍴ and probably will not work for anything else
    """
    A.noStringConfirm()

    if A.dimension() == 0:
        dimension = None

        if B.dimension() == 0:
            Rpy = 0
        else:
            Rpy = B.vectorToPy()[0]

    else:
        dimension = A.scalarToPy()

        if B.dimension() != 0:
            Rpy = Fn(dimension, B.vectorToPy())
        elif B.isString():
            Rpy = Fn(dimension, ' ')
        else:
            Rpy = Fn(dimension, [0])

    return aplQuantity(Rpy, dimension, B.isString())

# ------------------------------

def     vv_comma(Fn, A, B):
    """
    evaluate a dyadic function that returns a vector
    """
    case = A.isString() + B.isString()

    Apy = [A] if A.isString() and case == 1 else A.vectorToPy()
    Bpy = [B] if B.isString() and case == 1 else B.vectorToPy()

    Rpy = Fn(Apy, Bpy)

    return aplQuantity(Rpy, len(Rpy), case == 2)

# ------------------------------

def     sv_transpose(Fn, A, B):
    """
    evaluate dyadic transpose (a degenerate function for vectors)
    """
    A.noStringConfirm()

    if A.dimension() == 0 and B.isScalar():
        return B

    Apy = A.scalarToPy("LENGTH ERROR")

    if Apy != 1:
        aplError("DOMAIN ERROR")

    if B.isScalar():
        aplError("LENGTH ERROR")

    Bpy = B.vectorToPy()

    return aplQuantity(Fn(Apy, Bpy), B.dimension(), B.isString())

# ------------------------------

def     sv2vr(Fn, A, B):
    """
    evaluate a dyadic function that returns a vector if B is a vector but a scalar if B is scalar
    """
    A.noStringConfirm()

    if A.dimension() == 0:
        aplError("RANK ERROR")

    if B.dimension() == 0:
        return B

    Rpy = Fn(A.scalarToPy("RANK ERROR"), B.vectorToPy())

    if B.isScalar():
        return aplQuantity(Rpy[0], None, B.isString())

    if B.isVector():
        return aplQuantity(Rpy, B.dimension(), B.isString())

    aplError("RANK ERROR")

# ------------------------------

def     sv2vl(Fn, A, B):
    """
    evaluate a dyadic function that returns a vector if B is a vector but a scalar if B is scalar
    """
    A.noStringConfirm()

    if A.dimension() == 0:
        if B.isScalar():
            return B
        elif B.isVector():
            return aplQuantity([], 0, B.isString())

        aplError("RANK ERROR")

    if B.isString():
        Rpy = Fn(A.scalarToPy("LENGTH ERROR"), B.vectorToPy(), ord(' '))
    else:
        Rpy = Fn(A.scalarToPy("LENGTH ERROR"), B.vectorToPy(), 0)

    if B.isScalar() and Rpy != []:
        return aplQuantity(Rpy[0], None, B.isString())

    return aplQuantity(Rpy, len(Rpy), B.isString())

# ------------------------------

def     ce2v(Fn, A, B):
    """
    compress or expand a vector yielding another
    """
    A.noStringConfirm()

    if A.dimension() == 0 and B.isScalar():
        return aplQuantity([], 0, B.isString())

    if B.isString():
        Rpy = Fn(A.vectorToPy(), B.vectorToPy(), ord(' '))
    else:
        Rpy = Fn(A.vectorToPy(), B.vectorToPy(), 0)

    return aplQuantity(Rpy, len(Rpy), B.isString())

# ------------------------------

def     vv_match(Fn, A, B, noMatch):
    """
    match A and B
    """
    Rpy = 0

    if A.isString() != B.isString():
        Rpy = False

    elif A.dimension() != B.dimension():
        Rpy = False

    elif A.isScalar():
        Rpy = A.scalarToPy() == B.scalarToPy()

    elif A.isVector():
        Rpy = not next(filter(None, ss2s(Fn, A, B, False)), False)

    else:
        aplError("RANK ERROR")

    return aplQuantity(int(Rpy ^ noMatch), None)

# ------------------------------

def     vs2v_encode(Fn, A, B):
    """
    encode B to base A
    """
    A.noStringConfirm()
    B.noStringConfirm()

    if B.dimension() == 0:
        return aplQuantity([])

    Rpy = Fn(A.vectorToPy(), B.scalarToPy())

    if A.isScalar():
        return aplQuantity(Rpy[0], None, False)

    if A.isVector():
        return aplQuantity(Rpy, A.dimension(), False)

    aplError("RANK ERROR")

# ------------------------------

def     vv2s_decode(Fn, A, B):
    """
    decode B from base A
    """
    A.noStringConfirm()
    B.noStringConfirm()

    if A.isScalar():
        Rpy = Fn(iter(A), B.vectorToPy())
    else:
        Rpy = Fn(A.vectorToPy()[-B.dimension():], B.vectorToPy())

    return aplQuantity(Rpy, None, False)

# EOF
