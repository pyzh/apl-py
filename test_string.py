#!/usr/bin/python3
"""
    doctest style unit tests for strings

    WIP - grows as operators are implemented

    Each test passes a APL expression to the evaluate function.

    Each expression has one or two string operand.
"""

from evaluate import evaluate

from apl_cio import APL_cio as apl_cio
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
        cio = apl_cio()
        cio.printResult(evaluate(expr,cio))
    except apl_exception as error:
        print(error.message)

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

def     test_rho (expr):
    """
    >>> test_string("⍴ 'Hello'")
    5
    >>> test_string("⍴ 'Hello' 'Paul'")
    2
    >>> test_string("⍴ 1 'Hello' 2")
    3

    >>> test_string("⍴ 'H'")
    ⍬
    >>> test_string('⍴ "H"')
    1


    >>> test_string("4 ⍴ 'Hello'")
    Hell
    >>> test_string("5 ⍴ 'Hello'")
    Hello
    >>> test_string("6 ⍴ 'Hello'")
    HelloH
    """
    pass

# ------------------------------

def     test_comma (expr):
    """
    >>> test_string(", 'Hello'")
    Hello
    >>> test_string(", 'Hello' 'Paul'")
    'Hello' 'Paul'
    >>> test_string(", 1 'Hello' 2")
    1 'Hello' 2

    >>> test_string(", 'H'")
    H
    >>> test_string(', "H"')
    H

    >>> test_string("⍴, 'H'")
    1
    >>> test_string('⍴, "H"')
    1

    >>> test_string("'Hello' , ' ' , 'Paul'")
    Hello Paul

    >>> test_string("1 2 3 , 'Hello'")
    1 2 3 'Hello'
    >>> test_string("'Hello' , 1 2 3")
    'Hello' 1 2 3
    >>> test_string("1 2 3 , 'H'")
    1 2 3 'H'
    >>> test_string('1 2 3 , "H"')
    1 2 3 'H'
    """
    pass

# --------------

def     test_drop_take ():
    """
    >>> test_string('¯9 ↓ "abcdef"')
    <BLANKLINE>
    >>> test_string('¯6 ↓ "abcdef"')
    <BLANKLINE>
    >>> test_string('¯3 ↓ "abcdef"')
    abc
    >>> test_string('0 ↓ "abcdef"')
    abcdef
    >>> test_string('3 ↓ "abcdef"')
    def
    >>> test_string('6 ↓ "abcdef"')
    <BLANKLINE>
    >>> test_string('9 ↓ "abcdef"')
    <BLANKLINE>

    >>> test_string('¯9 ↑ "abcdef"')
       abcdef
    >>> test_string('¯6 ↑ "abcdef"')
    abcdef
    >>> test_string('¯3 ↑ "abcdef"')
    def
    >>> test_string('0 ↑ "abcdef"')
    <BLANKLINE>
    >>> test_string('3 ↑ "abcdef"')
    abc
    >>> test_string('6 ↑ "abcdef"')
    abcdef
    >>> test_string('(9 ↑ "abcdef"), "!"')
    abcdef   !

    >>> test_string('↓ ""')
    <BLANKLINE>
    >>> test_string('↑ ""')
    <BLANKLINE>
    >>> test_string('1 ↑ "Hello"')
    H
    >>> test_string('↑ "Hello"')
    H
    """
    pass

# --------------

def     test_reverse_rotate ():
    """
    >>> test_string('⌽ "niagara"')
    aragain
    >>> test_string('⊖ "nigeria"')
    airegin

    >>> test_string('1 ⌽ "nope"')
    open
    >>> test_string('2 ⊖ "anna"')
    naan

    >>> test_string('1 ⌽ "a"')
    a
    >>> test_string('2 ⊖ "b"')
    b

    >>> test_string('"H" ⌽ "nope"')
    DOMAIN ERROR
    >>> test_string('"Hi" ⊖ "anna"')
    DOMAIN ERROR
    """
    pass

# --------------

def     transpose ():
    """
    >>> test_string("'H' ⍉ 1 2 3")
    DOMAIN ERROR

    >>> test_string('⍉ "Hello"')
    Hello

    >>> test_string('1 ⍉ "Hello"')
    Hello
    """
    pass

# --------------

def     compress_expand ():
    """
    >>> test_string('1 0 1 / "ABC"')
    AC
    >>> test_string('1 2 3 / "ABC"')
    ABBCCC
    >>> test_string('1 ¯2 3 / "ABC"')
    A  CCC

    >>> test_string('1 0 1 0 1 \ "ABC"')
    A B C
    >>> test_string('1 0 2 0 3 \ "ABC"')
    A BB CCC
    >>> test_string('¯1 1 ¯2 1 ¯3 1 \ "ABC"')
     A  B   C
    """
    pass

# ------------------------------

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# EOF
