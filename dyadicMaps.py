"""
    map functions for dyadic APL functions

    UNDER DEVELOPMENT

    The functions in this module implement mathematical and non-mathematical
    dyadic APL functions for vectors in conjunction with an iterator object
    defined in dyadicIterators.

    Each function takes two APL quantities and returns a third.  The quantity
    returned is generally an iterator so implementing lazy evaluation.

    The mathematical APL functions are handled by the generic dyadicMap.  The
    pertinent scalar mathematical function is the first parameter.

    The non-mathematical APL functions the handled by special purpose map
    functions.  The pertinent iterator is the first parameter.

    Nested vectors are handled by recursion with the map function calling the
    iterator, which calls the map function.

    There are, of course, exceptions.  Scalar quantities are also handled as
    special cases.
"""

import operator

import dyadicIterators as iterator

from systemVariables import confirmInteger, indexOrigin

from makeQuantity import makeScalar, makeVector, makeEmptyVector, makeArray

from aplQuantity import aplQuantity
from aplIterators import scalarIterator, firstAxisIterator
from aplError import assertError, assertTrue, assertNotTrue
from aplError import assertNotScalar, assertNotVector, assertNotArray
from aplError import assertNumeric, assertScalarLike, assertEmptyVector

# ------------------------------

def     maths(Fn, A, B):
    """
    the basic recursive map for dyadic mathematical functions
    """
    if B.isArray():
        if A.isArray():
            # Check ranks are equal
            Rpy = iterator.maths(maths, Fn, A, B)

        elif A.isVector():
            # Check length is compatible
            Rpy = iterator.maths(maths, Fn, A.vectorIterator(), B)

        else:
            Rpy = iterator.maths(maths, Fn, A.scalarIterator(), B)

        return makeArray(Rpy, B.dimension(), B.prototype())

    if A.isArray():
        if B.isVector():
            # Check length is compatible
            Rpy = iterator.maths(maths, Fn, A, B.vectorIterator())

        else:
            Rpy = iterator.maths(maths, Fn, A, B.scalarIterator())

        return makeArray(Rpy, A.dimension(), A.prototype())

    if B.isVector():
        if A.isVector():
            if B.isEmptyVector():
                assertTrue(A.isEmptyVector(), "LENGTH ERROR")

            Rpy = iterator.maths(maths, Fn, A, B)

        elif B.isEmptyVector():
            return B

        else:
            Rpy = iterator.maths(maths, Fn, A.scalarIterator(), B)

        return makeVector(Rpy, B.dimension(), B.prototype())

    if A.isVector():
        if A.isEmptyVector():
            return A

        else:
            Rpy = iterator.maths(maths, Fn, A, B.scalarIterator())

        return makeVector(Rpy, A.dimension(), A.prototype())

    return makeScalar(iterator.maths(maths, Fn, A, B))

# ------------------------------

def     deal(Fn, A, B):
    """
    implement deal (dyadic ?)
    """
    assertScalarLike(A, "RANK ERROR")
    assertScalarLike(B, "RANK ERROR")

    Apy = confirmInteger(A.scalarToPy())

    return makeVector(Fn(Apy, B.scalarToPy()), Apy)

# ------------------------------

def     _matchMap(Fn, A, B):
    """
    the recursive map for dyadic ≡ and ≢

    returns a Boolean
    """
    if A.padFill() != B.padFill():
        return False

    elif A.isScalar():
        if B.isScalar():
            return all(iterator.match(_matchMap, Fn, A, B))

    elif A.isVector():
        if B.isVector():
            return all(iterator.match(_matchMap, Fn, A, B))

    else:
        if A.isArray():
            return all(iterator.match(_matchMap, Fn, A, B))

    return False

# --------------

def     match(Fn, A, B):
    """
    recursive implementation of dyadic ≢
    """
    return makeScalar(int(_matchMap(Fn, A, B)))

# --------------

def     noMatch(Fn, A, B):
    """
    recursive implementation of dyadic ≢
    """
    return makeScalar(int(not _matchMap(Fn, A, B)))

# ------------------------------

def     reshape(Fn, A, B):
    """
    implement dyadic ⍴
    """
    assertNotArray(A)

    if A.isScalarLike():
        Apy = confirmInteger(A.scalarToPy())

        assertTrue(Apy >= 0, "DOMAIN ERROR")

        if Apy == 0:
            return makeEmptyVector(B.prototype())

        Bpy = B.castToVectorPy()

        return makeVector(Fn(Apy, Bpy), Apy, B.prototype())

    if A.isEmptyVector():
        Bpy = B.castToVectorPy()

        return makeVector(Fn(1, Bpy), 1, B.prototype())

    Apy = tuple([confirmInteger(I) for I in A.vectorToPy()])

    assertTrue(Apy == (2, 2), "WIP - MATRIX ERROR")

    for I in Apy:
        assertTrue(I >= 0, "DOMAIN ERROR")

    Bpy = B.castToVectorPy()

    return makeArray(Fn(Apy, Bpy), Apy, 2 * B.prototype())

# ------------------------------

def     concatenate(Fn, A, B):
    """
    implement dyadic ,
    """
    assertNotArray(A, "WIP - RANK ERROR")
    assertNotArray(B, "WIP - RANK ERROR")

    prototype = B.prototype() if A.isEmptyVector() else A.prototype()

    Apy = 1 if A.isScalar() else A.dimension()
    Bpy = 1 if B.isScalar() else B.dimension()

    dimension = -1 if (Apy < 0 or Bpy < 0) else (Apy + Bpy)

    Rpy = Fn(A.vectorToPy(), B.vectorToPy())

    return makeVector(Rpy, dimension, prototype)

# ------------------------------

def     transpose(_, A, B):
    """
    implement dyadic ⍉
    """
    assertNotArray(A)

    if B.isScalar():
        assertEmptyVector(A)

        return B

    if B.isVector():
        assertScalarLike(A)

        Apy = confirmInteger(A.scalarToPy())

        assertTrue(Apy == 1, "DOMAIN ERROR")

        return B

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     rotate(Fn, A, B):
    """
    implement dyadic ⌽
    """
    assertNotArray(A)

    if B.isVectorLike():
        assertScalarLike(A, "RANK ERROR")

        Apy = confirmInteger(A.scalarToPy())

        if B.isEmptyVector():
            return B

        Apy = operator.mod(Apy, B.tally())

        if Apy == 0:
            return B

        return makeVector(Fn(Apy, B.vectorToPy()), B.dimension(), None)

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     partition(Fn, A, B):
    """
    implement dyadic ⊂
    """
    assertNotArray(A)

    assertNotTrue(B.isScalar(), "RANK ERROR")

    if B.isEmptyVector() and A.isEmptyVector():
        return B

    if B.isVector():
        if A.isScalar():
            Apy = confirmInteger(A.scalarToPy())

            if Apy == 0:
                return makeEmptyVector()

            return makeScalar((B,), B.prototype())

        return makeVector(Fn(A.vectorToPy(), B.vectorToPy()), -1, B.prototype())

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     pick(_, A, B):
    """
    implement dyadic ⊃
    """
    assertNotArray(A)
    assertNotArray(B)

    if A.isEmptyVector():
        return B

    assertNotScalar(B)

    if B.isVector():
        IO = indexOrigin()

        try:
            for X in A.vectorToPy():
                X = confirmInteger(X)

                assertTrue(X >= IO, "INDEX ERROR")

                if isinstance(B, aplQuantity):
                    B = B.vectorToPy()[X-IO]
                else:
                    assertError("RANK ERROR")

        except IndexError:
            assertError("INDEX ERROR")

        if isinstance(B, aplQuantity):
            return B

        return makeScalar((B,), None)

# ------------------------------

def     membership(Fn, A, B):
    """
    implement dyadic ∊
    """
    if A.isEmptyVector():
        return A

    Apy = A.arrayToPy() if A.isArray() else A.vectorToPy()
    Bpy = B.arrayToPy() if B.isArray() else B.vectorToPy()

    Rpy = Fn(Apy, Bpy)

    if A.isArray():
        return makeArray(Rpy, A.dimension(), A.prototype())

    if A.isVector():
        return makeVector(Rpy, A.dimension(), A.prototype())

    return makeScalar(Rpy, A.prototype())

# ------------------------------

def     find(Fn, A, B):
    """
    implement dyadic ∊
    """
    A.resolve()

    Apy = A.arrayToPy() if A.isArray() else A.vectorToPy()
    Bpy = B.arrayToPy() if B.isArray() else B.vectorToPy()

    Rpy = Fn(Apy, Bpy)

    if B.isArray():
        return makeArray(Rpy, B.dimension(), B.prototype())

    if B.isVector():
        return makeVector(Rpy, B.dimension(), B.prototype())

    return makeScalar(Rpy, B.prototype())

# ------------------------------

def     index(Fn, A, B):
    """
    implement dyadic ⍳
    """
    assertNotArray(A)

    if B.isEmptyVector():
        return makeEmptyVector(B.prototype())

    if A.isEmptyVector():
        Rpy = scalarIterator(indexOrigin(), B.elementCount(), B.expressionToGo)

    elif B.isArray():
        Rpy = Fn(A.vectorToPy(), B.arrayToPy())

    else:
        Rpy = Fn(A.vectorToPy(), B.vectorToPy())

    if B.isArray():
        return makeArray(Rpy, B.dimension())

    if B.isVector():
        return makeVector(Rpy, B.dimension())

    return makeScalar(Rpy)

# ------------------------------

def     without(Fn, A, B):
    """
    implement dyadic ~
    """
    assertNotArray(A)

    if B.isArray():
        Rpy = Fn(A.vectorToPy(), B.arrayToPy())

    else:
        Rpy = Fn(A.vectorToPy(), B.vectorToPy())

    return makeVector(Rpy, -1, A.prototype())

# ------------------------------

def     set2set(Fn, A, B):
    """
    implement dyadic ∪ and ∩
    """
    assertNotArray(A)
    assertNotArray(B)

    if A.isEmptyVector() and B.isEmptyVector():
        return B

    Rpy = Fn(A.vectorToPy(), B.vectorToPy())

    return makeVector(Rpy, -1, A.prototype())

# ------------------------------

def     drop(Fn, A, B):
    """
    implement dyadic ↓
    """
    assertNotArray(A)

    if B.isScalar():
        if A.isEmptyVector():
            return B

        assertScalarLike(A)

        Apy = confirmInteger(A.scalarToPy())

        if Apy == 0:
            return makeVector(B.vectorToPy(), 1, B.prototype())

        return makeEmptyVector(B.prototype())

    if B.isVector():
        if A.isEmptyVector():
            Apy = 1

        else:
            assertScalarLike(A)

            Apy = confirmInteger(A.scalarToPy())

            if Apy == 0:
                return B

        Rpy = Fn(Apy, B.vectorToPy())

        return makeVector(Rpy, -1, B.prototype())

    Apy = [confirmInteger(I) for I in A.vectorToPy()]

    assertTrue(B.dimension() == (2, 2), "WIP - MATRIX ERROR")

    assertTrue(len(Apy) == B.rank(), "LENGTH ERROR")

    Rpy = []
    for Bit in Fn(Apy[0], B.arrayByLastAxis()):
        Rpy += Fn(Apy[1], Bit.vectorToPy())

    return makeArray(Rpy, [max(0, I[1] - abs(I[0])) for I in zip(Apy, B.dimension())], B.prototype())

# ------------------------------

def     take(Fn, A, B):
    """
    implement dyadic ↑
    """
    assertNotArray(A)

    if B.isScalar() or B.isEmptyVector():
        if A.isEmptyVector():
            return B

    if B.isVectorLike():
        assertScalarLike(A)

        Apy = confirmInteger(A.scalarToPy())

        if Apy == 0:
            return makeEmptyVector(B.prototype())

        Rpy = Fn(Apy, B.vectorToPy(), B.padFill())

        return makeVector(Rpy, abs(Apy), B.prototype())

    Apy = [confirmInteger(I) for I in A.vectorToPy()]

    assertTrue(B.dimension() == (2, 2), "WIP - MATRIX ERROR")

    assertTrue(len(Apy) == B.rank(), "LENGTH ERROR")

    Rpy = []
    for Bit in Fn(Apy[0], B.arrayByLastAxis(), B.padFill()):
        Rpy += Fn(Apy[1], Bit.vectorToPy(), Bit.padFill())

    return makeArray(Rpy, [abs(I) for I in Apy], B.prototype())

# ------------------------------

def     compress(Fn, A, B):
    """
    implement dyadic /
    """
    assertNotArray(A)

    if B.isScalar() and A.isEmptyVector():
        return makeEmptyVector(B.prototype())

    if B.isVectorLike():
        Rpy = Fn(A.promoteScalarToVectorPy(), B.vectorToPy(), B.padFill())

        return makeVector(Rpy, -1, B.prototype())

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     expand(Fn, A, B):
    """
    implement dyadic /
    """
    assertNotArray(A)

    if B.isScalar() and A.isEmptyVector():
        return makeEmptyVector(B.prototype())

    if B.isVectorLike():
        if A.isScalar():
            Apy = confirmInteger(A.scalarToPy())

            assertTrue(Apy >= 0, "LENGTH ERROR")

            if Apy == 0:
                return makeVector(B.prototype(), 1, B.prototype())

        Rpy = Fn(A.promoteScalarToVectorPy(), B.vectorToPy(), B.padFill())

        return makeVector(Rpy, -1, B.prototype())

    assertNotArray(B, "WIP - RANK ERROR")

# ------------------------------

def     encode(Fn, A, B):
    """
    implement dyadic ⊤
    """
    if B.isEmptyVector():
        # Simplistic
        return makeEmptyVector()

    if A.isEmptyVector():
        # Simplistic
        return makeEmptyVector()

    if B.isArray():
        if A.isScalarLike():
            Rpy = []
            Apy = A.vectorToPy()
            for Bpy in B.arrayToPy():
                Rpy.append(Fn(Apy, Bpy).__next__())

            return makeArray(Rpy, B.dimension())

        assertError("WIP - RANK ERROR")

    if B.isVector():
        assertTrue(B.tally() == 2, "WIP - LENGTH ERROR")

        if A.isArray():
            assertError("WIP - RANK ERROR")

        if A.isVector():
            assertTrue(A.tally() == 2, "WIP - LENGTH ERROR")

            Rpy, Apy = [], A.vectorToPy()
            for Bpy in B.vectorToPy():
                Rpy += Fn(Apy, Bpy)

            Rpy, Tpy = [], Rpy
            for Bit in firstAxisIterator(Tpy, A.tally()):
                Rpy += Bit.vectorToPy()

            return makeArray(Rpy, (A.tally(), B.tally()))

        Rpy, Apy = [], A.vectorToPy()
        for Bpy in B.vectorToPy():
            Rpy += Fn(Apy, Bpy)

    if A.isArray():
        Rpy, Bpy = [], B.scalarToPy()
        for Ait in A.arrayByFirstAxis():
            Rpy += Fn(Ait.vectorToPy(), Bpy)

        return makeArray(Rpy, A.dimension(), B.prototype())

    if A.isVector():
        Rpy = Fn(A.vectorToPy(), B.scalarToPy())

        return makeVector(Rpy, A.tally())

    Rpy = Fn(A.vectorToPy(), B.scalarToPy())

    return makeScalar(Rpy)

# ------------------------------

def     decode(Fn, A, B):
    """
    implement dyadic ⊥
    """
    if B.isArray():
        if A.isScalarLike():
            Rpy = []
            for Bit in B.arrayByFirstAxis():
                Rpy.append(Fn(A.promoteScalarToVectorPy(), Bit))

            return makeVector(Rpy, B.dimension()[0], B.prototype())

        if A.isVector():
            assertNotTrue(A.isEmptyVector(), "DOMAIN ERROR")
            assertTrue(A.tally() == B.dimension()[0], "LENGTH ERROR")

            Rpy = []
            for Bit in B.arrayByFirstAxis():
                Rpy.append(Fn(A.vectorToPy(), Bit))

            return makeVector(Rpy, A.dimension(), B.prototype())

        assertTrue(A.rank() == B.rank(), "WIP - RANK ERROR")

        assertTrue(A.dimension()[-1] == B.dimension()[0], "LENGTH ERROR")

        Rpy = []
        for Ait in A.arrayByLastAxis():
            for Bit in B.arrayByFirstAxis():
                Rpy.append(Fn(Ait, Bit))

        return makeArray(Rpy, A.dimension(), B.prototype())

    if B.isVector():
        if A.isEmptyVector() or B.isEmptyVector():
            return makeScalar(0)

        return makeScalar(Fn(A.promoteScalarToVectorPy(), B.vectorToPy()))

    if A.isScalar():
        assertNumeric(A)
        assertNumeric(B)

        return B

    return makeScalar(Fn(A.vectorToPy(), B.scalarIterator()))

# ------------------------------

def     grade(descending, A, B):
    """
    implement dyadic ⍒ and ⍋
    """
    def _sortKey(X):
        """
        sort key is the collation sequence index
        """
        Y = Bpy[X]
        try:
            return Apy.index(Y)
        except ValueError:
            return Len

    assertNotScalar(B, "RANK ERROR")

    if B.isVectorLike():
        A.resolve()
        assertTrue(A.isString(), "DOMAIN ERROR")
        Apy = A.vectorToPy()

        B.resolve()
        assertTrue(B.isString(), "DOMAIN ERROR")
        Len = B.tally()
        Bpy = B.vectorToPy()

        S = list(range(Len))
        S.sort(key=_sortKey, reverse=descending)

        return makeVector(iterator.grade(S), Len)

    assertNotArray(B, "WIP - RANK ERROR")

# EOF
