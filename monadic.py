#!/usr/bin/python3
"""
    monadic APL functions

    WIP - limited set

    WIP - scalar parameters only
"""

import operator

from apl_exception import APL_Exception as apl_exception

# ------------------------------

def     identity (B):
    """
    identity

    scalar argument only
    """
    return operator.pos(B)

def     negation (B):
    """
    change sign of B

    scalar argument only
    """
    return operator.neg(B)

def     signum (B):
    """
    sign of B

    scalar argument only
    """
    if B > 0:   return 1
    if B < 0:   return -1

    return 0

def     reciprocal (B):
    """
    1 divided by B

    scalar argument only

    throws RANGE ERROR (B == 0)
    """
    try:
        return operator.truediv(1.0,B)
    except:
        raise (apl_exception("RANGE ERROR"))

# ------------------------------

def     logical_negation (B):
    """
    Boolean integer inverse of B

    scalar argument only

    throws DOMAIN ERROR (B is not 0 or 1)
    """
    if B == 1:  return 0
    if B == 0:  return 1

    raise (apl_exception("DOMAIN ERROR"))

# ------------------------------

def     to_be_implemented (B):
    """
    placeholder for functions not yet implemented

    throws FUNCTION NOT YET IMPLEMENTED
    """
    raise (apl_exception("FUNCTION NOT YET IMPLEMENTED"))

# ------------------------------

monadic_functions = {
    '+':        identity,
    '-':        negation,
    '×':        signum,
    '÷':        reciprocal,

    '~':        logical_negation,

    '?':        to_be_implemented,      # roll
    '⌈':        to_be_implemented,      # ceiling
    '⌊':        to_be_implemented,      # floor
    '⍴':        to_be_implemented,      # shape
    '∣':        to_be_implemented,      # absolute value
    '⍳':        to_be_implemented,      # index generator
    '*':        to_be_implemented,      # exponential
    ',':        to_be_implemented,      # reshape into a vector
    '⌹':        to_be_implemented,      # matrix inverse
    '○':        to_be_implemented,      # pi times
    '⍟':        to_be_implemented,      # natural logarithm
    '⌽':        to_be_implemented,      # reversal, last axis
    '⊖':        to_be_implemented,      # reversal, first axis
    '⍋':        to_be_implemented,      # grade up
    '⍒':        to_be_implemented,      # grade down
    '⍎':        to_be_implemented,      # execute
    '⍕':        to_be_implemented,      # monadic format
    '⍉':        to_be_implemented,      # transpose
    '!':        to_be_implemented,      # factorial
    };

def     monadic_function (symbol):
    """
    return the monadic function given its APL symbol

    throws INVALID TOKEN if the symbol is not recognised
    """
    try:
        return monadic_functions[symbol[0]]
    except KeyError:
        raise (apl_exception("INVALID TOKEN", symbol))

# EOF
