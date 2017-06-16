#!/usr/bin/python3
"""
    Unit test for strings - doctest style

    WIP - grows as operators are implemented
"""

from evaluate import evaluate

from apl import print_result

from apl_error import APL_exception as apl_exception

# ------------------------------

def     test_string (expr):
    """
    >>> test_string("'Hello'")
    Hello
    >>> test_string("'Hello\\"Jello'")
    Hello"Jello
    >>> test_string("'Hello''Jello'")
    Hello'Jello
    >>> test_string("'H'")
    H
    >>> test_string("''")
    <BLANKLINE>

    >>> test_string('"Hello"')
    Hello
    >>> test_string('"Hello\\'Jello"')
    Hello'Jello
    >>> test_string('"Hello""Jello"')
    Hello"Jello
    >>> test_string('"H"')
    H
    >>> test_string('""')
    <BLANKLINE>

    >>> test_string("'Hello'")
    Hello
    >>> test_string("'Hello' 'Paul'")
    'Hello' 'Paul'
    >>> test_string("1 'Hello' 2")
    1 'Hello' 2
    >>> test_string("'Hello' (19 20) 'Paul'")
    'Hello' (19 20) 'Paul'
    """
    try:
        print_result(evaluate(expr))
    except apl_exception as error:
        print (error.message)

# ------------------------------

def     test_monadic_arithmetic (expr):
    """
    >>> test_string("+ 'Hello'")
    DOMAIN ERROR
    >>> test_string("- 'Hello'")
    DOMAIN ERROR
    >>> test_string("× 'Hello'")
    DOMAIN ERROR
    >>> test_string("÷ 'Hello'")
    DOMAIN ERROR

    >>> test_string("⌈ 'Hello'")
    DOMAIN ERROR
    >>> test_string("⌊ 'Hello'")
    DOMAIN ERROR
    >>> test_string("| 'Hello'")
    DOMAIN ERROR

    >>> test_string("* 'Hello'")
    DOMAIN ERROR
    >>> test_string("⍟ 'Hello'")
    DOMAIN ERROR
    >>> test_string("? 'Hello'")
    DOMAIN ERROR
    >>> test_string("! 'Hello'")
    DOMAIN ERROR

    >>> test_string("⌹ 'Hello'")
    FUNCTION NOT YET IMPLEMENTED
    >>> test_string("○ 'Hello'")
    DOMAIN ERROR
    """
    pass

# ------------------------------

def     test_dyadic_arithmetic (expr):
    """
    >>> test_string("1 + 'Hello'")
    DOMAIN ERROR
    >>> test_string("1 - 'Hello'")
    DOMAIN ERROR
    >>> test_string("1 × 'Hello'")
    DOMAIN ERROR
    >>> test_string("1 ÷ 'Hello'")
    DOMAIN ERROR

    >>> test_string("'Hello' + 1")
    DOMAIN ERROR
    >>> test_string("'Hello' - 1")
    DOMAIN ERROR
    >>> test_string("'Hello' × 1")
    DOMAIN ERROR
    >>> test_string("'Hello' ÷ 1")
    DOMAIN ERROR

    >>> test_string("1 ⌈ 'Hello'")
    DOMAIN ERROR
    >>> test_string("1 ⌊ 'Hello'")
    DOMAIN ERROR
    >>> test_string("1 | 'Hello'")
    DOMAIN ERROR

    >>> test_string("1 * 'Hello'")
    DOMAIN ERROR
    >>> test_string("1 ⍟ 'Hello'")
    DOMAIN ERROR
    >>> test_string("1 ? 'Hello'")
    RANK ERROR
    >>> test_string("1 ! 'Hello'")
    DOMAIN ERROR

    >>> test_string("1 ⌹ 'Hello'")
    FUNCTION NOT YET IMPLEMENTED
    >>> test_string("1 ○ 'Hello'")
    DOMAIN ERROR

    >>> test_string("1 ∨ 'Hello'")
    DOMAIN ERROR
    >>> test_string("1 ∧ 'Hello'")
    DOMAIN ERROR
    >>> test_string("1 ⍱ 'Hello'")
    DOMAIN ERROR
    >>> test_string("1 ⍲ 'Hello'")
    DOMAIN ERROR

    >>> test_string("1 < 'Hello'")
    DOMAIN ERROR
    >>> test_string("1 ≤ 'Hello'")
    DOMAIN ERROR
    >>> test_string("1 ≥ 'Hello'")
    DOMAIN ERROR
    >>> test_string("1 > 'Hello'")
    DOMAIN ERROR

    >>> test_string("1 = 'Hello'")
    0 0 0 0 0
    >>> test_string("1 ≠ 'Hello'")
    1 1 1 1 1
    >>> test_string("'Hello' = 'Hello'")
    1 1 1 1 1
    >>> test_string("'hello' ≠ 'Hello'")
    1 0 0 0 0
    >>> test_string("'H' = 72")
    1
    >>> test_string('"H" ≠ 72')
    0
    >>> test_string("'Hello' = 'Goodbye'")
    LENGTH ERROR
    >>> test_string("'Hello' ≠ 'Goodbye'")
    LENGTH ERROR

    >>> test_string("1 ≡ 'Hello'")
    FUNCTION NOT YET IMPLEMENTED
    """
    pass

# ------------------------------

def     test_tilda (expr):
    """
    >>> test_string("~ 'Hello'")
    DOMAIN ERROR

    >>> test_string("1 ~ 'Hello'")
    1
    >>> test_string("'Hello' ~ 1")
    Hello
    >>> test_string("'Hello' ~ 'hello'")
    H

    >>> test_string("'Hello' ~ 'Hello'")
    <BLANKLINE>
    """
    pass

# ------------------------------

def     test_iota (expr):
    """
    >>> test_string("⍳ 'Hello'")
    DOMAIN ERROR

    >>> test_string("1 ⍳ 'Hello'")
    2 2 2 2 2
    >>> test_string("'Hello' ⍳ 1")
    6
    >>> test_string("'Hello' ⍳ 'hello'")
    6 2 3 3 5

    >>> test_string("'Hello' ⍳ 72")
    6
    """
    pass

# ------------------------------

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# EOF