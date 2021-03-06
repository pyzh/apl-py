#!/usr/bin/python3
"""
    doctest style unit tests for APL dyadic functions

    WIP - grows as more dyadic functions are implemented.

    The tests in this module exercise dyadic functions with

        numeric scalar and vector arguments only.

    Other cases are covered in other test modules.

    Each test passes an APL expression to the evaluate function.
    Both positive and negative (e.g. DOMAIN ERROR) cases are tested.

    Note:
        testDyadic --eager      # run with eager evaluation
        testDyadic --lazy       # run with lazy evaluation
"""

from test.base import preamble, testResult as test
from test.base import saveIndexOrigin, setIndexOrigin, restoreIndexOrigin

# ------------------------------

def     dyadic():
    """
    >>> test(r"1 ⌹ 1")
    FUNCTION NOT YET IMPLEMENTED

    >>> test(r"1 ¯ 1")
    INVALID TOKEN
    """
    pass

# ------------------------------

def     conjugate_plus():
    """
    >>> test(r"1 + 1")
    2
    >>> test(r"0.5 + 0 0.5 1 2")
    0.5 1 1.5 2.5
    >>> test(r"¯0 ¯0.5 ¯1 ¯2 + 0.5")
    0.5 0 ¯0.5 ¯1.5

    >>> test(r"0 0.5 1 2 + 0 0.5 1 2")
    0 1 2 4
    >>> test(r"¯0 ¯0.5 ¯1 ¯2 + ¯0 ¯0.5 ¯1 ¯2")
    0 ¯1 ¯2 ¯4
    >>> test(r"0 0.5 1 2 + ¯0 ¯0.5 ¯1 ¯2")
    0 0 0 0
    >>> test(r"¯0 ¯0.5 ¯1 ¯2 + 0 0.5 1 2")
    0 0 0 0

    >>> test(r"1.2 + ,1.2")
    2.4
    >>> test(r"⍴ 1.2 + ,1.2")
    1
    >>> test(r"⍴ (,1.2) + 1.2")
    1

    >>> test(r"1 2 + 1")
    2 3
    >>> test(r"1 2 + ,1")
    LENGTH ERROR
    """
    pass

# --------------

def     negate_minus():
    """
    >>> test(r"1 - 1")
    0
    >>> test(r"0.5 - 0 0.5 1 2")
    0.5 0 ¯0.5 ¯1.5
    >>> test(r"¯0 ¯0.5 ¯1 ¯2 - 0.5")
    ¯0.5 ¯1 ¯1.5 ¯2.5

    >>> test(r"0 0.5 1 2 - 0 0.5 1 2")
    0 0 0 0
    >>> test(r"¯0 ¯0.5 ¯1 ¯2 - ¯0 ¯0.5 ¯1 ¯2")
    0 0 0 0
    >>> test(r"0 0.5 1 2 - ¯0 ¯0.5 ¯1 ¯2")
    0 1 2 4
    >>> test(r"¯0 ¯0.5 ¯1 ¯2 - 0 0.5 1 2")
    0 ¯1 ¯2 ¯4

    >>> test(r"1.2 - ,1.2")
    0
    >>> test(r"⍴ 1.2 - ,1.2")
    1
    >>> test(r"⍴ (,1.2) + 1.2")
    1

    >>> test(r"1 2 - 1")
    0 1
    >>> test(r"1 2 - ,1")
    LENGTH ERROR
    """
    pass

# --------------

def     direction_times():
    """
    >>> test(r"1 × 1")
    1
    >>> test(r"0.5 × 0 0.5 1 2")
    0 0.25 0.5 1
    >>> test(r"¯0 ¯0.5 ¯1 ¯2 × 0.5")
    0 ¯0.25 ¯0.5 ¯1

    >>> test(r"0 0.5 1 2 × 0 0.5 1 2")
    0 0.25 1 4
    >>> test(r"¯0 ¯0.5 ¯1 ¯2 × ¯0 ¯0.5 ¯1 ¯2")
    0 0.25 1 4
    >>> test(r"0 0.5 1 2 × ¯0 ¯0.5 ¯1 ¯2")
    0 ¯0.25 ¯1 ¯4
    >>> test(r"¯0 ¯0.5 ¯1 ¯2 × 0 0.5 1 2")
    0 ¯0.25 ¯1 ¯4

    >>> test(r"1.2 × ,1.2")
    1.44
    >>> test(r"⍴ 1.2 × ,1.2")
    1
    >>> test(r"⍴ (,1.2) + 1.2")
    1

    >>> test(r"1 2 × 1")
    1 2
    >>> test(r"1 2 × ,1")
    LENGTH ERROR
    """
    pass

# --------------

def     reciprocal_divide():
    """
    >>> test(r"0 ÷ 0")
    1
    >>> test(r"1 ÷ 0")
    DOMAIN ERROR
    >>> test(r"0 ÷ 1")
    0
    >>> test(r"1 ÷ 1")
    1

    >>> test(r"0.5 ÷ 0.25 0.5 1 2")
    2 1 0.5 0.25
    >>> test(r"¯0.25 ¯0.5 ¯1 ¯2 ÷ 0.5")
    ¯0.5 ¯1 ¯2 ¯4

    >>> test(r"0 0.5 1 2 ÷ 0.25 0.5 1 2")
    0 1 1 1
    >>> test(r"¯0 ¯0.5 ¯1 ¯2 ÷ ¯0.25 ¯0.5 ¯1 ¯2")
    0 1 1 1
    >>> test(r"0 0.5 1 2 ÷ ¯0.25 ¯0.5 ¯1 ¯2")
    0 ¯1 ¯1 ¯1
    >>> test(r"¯0 ¯0.5 ¯1 ¯2 ÷ 0.25 0.5 1 2")
    0 ¯1 ¯1 ¯1

    >>> test(r"1.2 ÷ ,1.2")
    1
    >>> test(r"⍴ 1.2 ÷ ,1.2")
    1
    >>> test(r"⍴ (,1.2) + 1.2")
    1

    >>> test(r"1 2 ÷ 1")
    1 2
    >>> test(r"1 2 ÷ ,1")
    LENGTH ERROR
    """
    pass

# --------------

def     ceil_maximum():
    """
    >>> test(r"1 ⌈ 1")
    1

    >>> test(r"0.5 ⌈ 0.25 0.5 1.9 2.1")
    0.5 0.5 1.9 2.1
    >>> test(r"¯0.25 ¯0.5 ¯1.9 ¯2.1 ⌈ 0.5")
    0.5 0.5 0.5 0.5

    >>> test(r"0.25 0.5 1.1 9.9 ⌈ 0.25 0.5 1.1 9.9")
    0.25 0.5 1.1 9.9
    >>> test(r"¯0.25 ¯0.5 ¯1.1 ¯9.9 ⌈ ¯0.25 ¯0.5 ¯1.1 ¯9.9")
    ¯0.25 ¯0.5 ¯1.1 ¯9.9
    >>> test(r"0.25 0.5 1.1 9.9 ⌈ ¯0.25 ¯0.5 ¯1.1 ¯9.9")
    0.25 0.5 1.1 9.9
    >>> test(r"¯0.25 ¯0.5 ¯1.1 ¯9.9 ⌈ 0.25 0.5 1.1 9.9")
    0.25 0.5 1.1 9.9
    """
    pass

# --------------

def     floor_minimum():
    """
    >>> test(r"1 ⌊ 1")
    1

    >>> test(r"0.5 ⌊ 0.25 0.5 1.9 2.1")
    0.25 0.5 0.5 0.5
    >>> test(r"¯0.25 ¯0.5 ¯1.1 ¯9.9 ⌊ 0.5")
    ¯0.25 ¯0.5 ¯1.1 ¯9.9

    >>> test(r"0.25 0.5 1.1 9.9 ⌊ 0.25 0.5 1.1 9.9")
    0.25 0.5 1.1 9.9
    >>> test(r"¯0.25 ¯0.5 ¯1.1 ¯9.9 ⌊ ¯0.25 ¯0.5 ¯1.1 ¯9.9")
    ¯0.25 ¯0.5 ¯1.1 ¯9.9
    >>> test(r"0.25 0.5 1.1 9.9 ⌊ ¯0.25 ¯0.5 ¯1.1 ¯9.9")
    ¯0.25 ¯0.5 ¯1.1 ¯9.9
    >>> test(r"¯0.25 ¯0.5 ¯1.1 ¯9.9 ⌊ 0.25 0.5 1.1 9.9")
    ¯0.25 ¯0.5 ¯1.1 ¯9.9
    """
    pass

# --------------

def     magnitude_residue():
    """
    >>> test(r"0 | 0")
    0
    >>> test(r"1 | 1")
    0

    >>> test(r"0.5 | 0.25 0.5 1.9 2.1")
    0.25 0 0.4 0.1
    >>> test(r"¯0.25 ¯0.5 ¯1.9 ¯2.1 | 0.5")
    0 0 ¯1.4 ¯1.6

    >>> test(r"0.25 0.5 1.9 2.1 | 0.25 0.5 1.9 2.1")
    0 0 0 0
    >>> test(r"¯0.25 ¯0.5 ¯1.9 ¯2.1 | ¯0.25 ¯0.5 ¯1.9 ¯2.1")
    0 0 0 0
    >>> test(r"0.25 0.5 1.9 2.1 | ¯0.25 ¯0.5 ¯1.9 ¯2.1")
    0 0 0 0
    >>> test(r"¯0.25 ¯0.5 ¯1.9 ¯2.1 | 0.25 0.5 1.9 2.1")
    0 0 0 0

    >>> test(r"TEN ← 1 2 3 4 5 6 7 8 9 10")
    1 2 3 4 5 6 7 8 9 10

    >>> test(r"(TEN) | 10")
    0 0 1 2 0 4 3 2 1 0
    >>> test(r"(-TEN) | 10")
    0 0 ¯2 ¯2 0 ¯2 ¯4 ¯6 ¯8 0
    """
    pass

# ------------------------------

def     exponential_power():
    """
    >>> test(r"0 * ¯1")
    DOMAIN ERROR
    >>> test(r"¯2 ¯1 0 1 2 * 0")
    1 1 1 1 1

    >>> test(r"1 * 0 0.5 1 2")
    1 1 1 1
    >>> test(r"¯0 ¯0.5 ¯1 ¯2 * 1")
    0 ¯0.5 ¯1 ¯2

    >>> test(r"0 0.5 1 2 * 0 0.5 1 2")
    1 0.7071067812 1 4
    >>> test(r"¯0 ¯0.5 ¯1 ¯2 * ¯0 ¯0.5 ¯1 ¯2")
    DOMAIN ERROR
    >>> test(r"0 0.5 1 2 * ¯0 ¯0.5 ¯1 ¯2")
    1 1.414213562 1 0.25
    >>> test(r"¯0 ¯0.5 ¯1 ¯2 * 0 0.5 1 2")
    DOMAIN ERROR
    """
    pass

# --------------

def     logarithm():
    """
    >>> test(r"0 ⍟ ¯1 0 1")
    0 1 0

    >>> test(r"1 ⍟ ¯1")
    DOMAIN ERROR
    >>> test(r"1 ⍟ 0")
    DOMAIN ERROR
    >>> test(r"1 ⍟ 1")
    1

    >>> test(r"¯1 ⍟ 0")
    DOMAIN ERROR
    >>> test(r"¯1 ⍟ ¯1 1")
    1 0

    >>> test(r"1 ⍟ 0 0.5 1 2")
    DOMAIN ERROR
    >>> test(r"¯0 ¯0.5 ¯1 ¯2 ⍟ 1")
    0 0 0 0

    >>> test(r"0 0.5 1 2 ⍟ 0 0.5 1 2")
    1 1 1 1
    >>> test(r"¯0 ¯0.5 ¯1 ¯2 ⍟ ¯0 ¯0.5 ¯1 ¯2")
    1 1 1 1
    >>> test(r"0 0.5 1 2 ⍟ ¯0 ¯0.5 ¯1 ¯2")
    DOMAIN ERROR
    >>> test(r"¯0 ¯0.5 ¯1 ¯2 ⍟ 0 0.5 1 2")
    DOMAIN ERROR

    >>> test(r"2 ⍟ 0.5 2 4 16 256 1024")
    ¯1 1 2 4 8 10
    >>> test(r"10 ⍟ 0.1 10 1000 1000000")
    ¯1 1 3 6
    """
    pass

# --------------

def     factorial_binomial():
    """
    >>> test(r"1 ? 1")
    1
    >>> test(r"1 ? ,1")
    1

    >>> test(r"⍴ 1 ? 1")
    1
    >>> test(r"⍴ 1 ? ,1")
    1

    >>> test(r"¯1 ! ¯1 0 1")
    1 0 0
    >>> test(r"0 ! ¯1 0 1")
    1 1 1
    >>> test(r"1 ! ¯1 0 1")
    ¯1 0 1

    >>> test(r"1 ! 0 0.5 1 2")
    0 0.5 1 2
    >>> test(r"¯0 ¯0.5 ¯1 ¯2 ! 1")
    1 0.4244131816 0 0

    >>> test(r"0 0.5 1 2 ! 0 0.5 1 2")
    1 1 1 1
    >>> test(r"¯0 ¯0.5 ¯1 ¯2 ! ¯0 ¯0.5 ¯1 ¯2")
    1 1 1 1
    >>> test(r"0 0.5 1 2 ! ¯0 ¯0.5 ¯1 ¯2")
    1 0 ¯1 3
    >>> test(r"¯0 ¯0.5 ¯1 ¯2 ! 0 0.5 1 2")
    1 0.5 0 0

    >>> test(r"0 1 2 3 4 ! 4")
    1 4 6 4 1
    >>> test(r"0 1 2 3 4 5 ! 5")
    1 5 10 10 5 1
    """
    pass

# --------------

def     roll_deal():
    """
    randomness makes positive testing a little tricky

    >>> test(r"1 ? 1")
    1
    >>> test(r"1 ? ,1")
    1

    >>> test(r"⍴ 1 ? 1")
    1
    >>> test(r"⍴ 1 ? ,1")
    1

    >>> test(r"1 ? ¯1")
    DOMAIN ERROR
    >>> test(r"1 ? 0")
    DOMAIN ERROR
    >>> test(r"1 ? 1")
    1

    >>> test(r"0.5 ? 2")
    DOMAIN ERROR
    >>> test(r"1 ? 1.5")
    DOMAIN ERROR

    >>> test(r"2 ? 1")
    DOMAIN ERROR

    >>> test(r"1 ? 10 10")
    RANK ERROR
    >>> test(r"1 1 ? 10")
    RANK ERROR
    """
    pass

# ------------------------------

def     pi_circular():
    """
    only run tests that return real number - ignore the imaginary results for now

    >>> test(r"B ← ○ ¯2 ¯1.5 ¯1 ¯0.5 0 0.5 1 1.5 2")
    ¯6.283185307 ¯4.71238898 ¯3.141592654 ¯1.570796327 0 1.570796327 3.141592654 4.71238898 6.283185307

    >>> test(r"1 ○ B")
    2.449293598e¯16 1 ¯1.224646799e¯16 ¯1 0 1 1.224646799e¯16 ¯1 ¯2.449293598e¯16
    >>> test(r"2 ○ B")
    1 ¯1.836970199e¯16 ¯1 6.123233996e¯17 1 6.123233996e¯17 ¯1 ¯1.836970199e¯16 1
    >>> test(r"3 ○ B")
    2.449293598e¯16 ¯5.443746451e+15 1.224646799e¯16 ¯1.633123935e+16 0 1.633123935e+16 ¯1.224646799e¯16 5.443746451e+15 ¯2.449293598e¯16

    >>> test(r"5 ○ B")
    ¯267.744894 ¯55.6543976 ¯11.54873936 ¯2.301298902 0 2.301298902 11.54873936 55.6543976 267.744894
    >>> test(r"6 ○ B")
    267.7467615 55.66338089 11.59195328 2.509178479 1 2.509178479 11.59195328 55.66338089 267.7467615
    >>> test(r"7 ○ B")
    ¯0.9999930253 ¯0.999838614 ¯0.9962720762 ¯0.9171523357 0 0.9171523357 0.9962720762 0.999838614 0.9999930253

    !>>> test(r"¯1 ○ B")
    ¯1.570796327J2.52463066 ¯1.570796327J2.231889253 ¯1.570796327J1.811526272 ¯1.570796327J1.023227479 0 1.570796327J¯1.023227479 1.570796327J¯1.811526272 1.570796327J¯2.231889253 1.570796327J¯2.52463066
    !>>> test(r"¯2 ○ B")
    3.141592654J2.52463066 3.141592654J2.231889253 3.141592654J1.811526272 3.141592654J1.023227479 1.570796327 0J¯1.023227479 0J¯1.811526272 0J¯2.231889253 0J¯2.52463066
    !>>> test(r"¯3 ○ B")
    ¯1.412965137 ¯1.361691683 ¯1.262627256 ¯1.003884822 0 1.003884822 1.262627256 1.361691683 1.412965137

    >>> test(r"¯1 ○ 0")
    0
    >>> test(r"¯2 ○ 0")
    1.570796327
    >>> test(r"¯3 ○ B")
    ¯1.412965137 ¯1.361691683 ¯1.262627256 ¯1.003884822 0 1.003884822 1.262627256 1.361691683 1.412965137

    !>>> test(r"¯5 ○ B")
    ¯2.537297501 ¯2.254414593 ¯1.862295743 ¯1.233403118 0 1.233403118 1.862295743 2.254414593 2.537297501
    !>>> test(r"¯6 ○ B")
    2.52463066J3.141592654 2.231889253J3.141592654 1.811526272J3.141592654 1.023227479J3.141592654 0J1.570796327 1.023227479 1.811526272 2.231889253 2.52463066
    !>>> test(r"¯7 ○ B")
    ¯0.1605195575J1.570796327 ¯0.2154808611J1.570796327 ¯0.329765315J1.570796327 ¯0.7524692671J1.570796327 0 0.7524692671J¯1.570796327 0.329765315J¯1.570796327 0.2154808611J¯1.570796327 0.1605195575J¯1.570796327

    >>> test(r"¯5 ○ B")
    ¯2.537297501 ¯2.254414593 ¯1.862295743 ¯1.233403118 0 1.233403118 1.862295743 2.254414593 2.537297501
    >>> test(r"¯6 ○ ○ 0.5 1 1.5 2")
    1.023227479 1.811526272 2.231889253 2.52463066
    >>> test(r"¯7 ○ 0")
    0

    !>>> test(r"0 ○ B")
    0J6.20309742 0J4.605063507 0J2.978188107 0J1.211363323 1 0J¯1.211363323 0J¯2.978188107 0J¯4.605063507 0J¯6.20309742
    >>> test(r"0 ○ 0")
    1
    >>> test(r"4 ○ B")
    6.362265132 4.817323936 3.296908309 1.862095889 1 1.862095889 3.296908309 4.817323936 6.362265132
    >>> test(r"¯4 ○ B", True)
    DOMAIN ERROR
    """
    pass

# ------------------------------

def     or_gcd():
    """
    >>> test(r"0 ∨ 0 1")
    0 1
    >>> test(r"1 ∨ 0 1")
    1 1

    >>> test(r"TEN ← 1 2 3 4 5 6 7 8 9 10")
    1 2 3 4 5 6 7 8 9 10

    >>> test(r"(TEN) ∨ 10")
    1 2 1 2 5 2 1 2 1 10
    >>> test(r"(-TEN) ∨ 10")
    1 2 1 2 5 2 1 2 1 10
    >>> test(r"(TEN) ∨ ¯10")
    1 2 1 2 5 2 1 2 1 10
    >>> test(r"(-TEN) ∨ ¯10")
    1 2 1 2 5 2 1 2 1 10

    >>> test(r"7.5 ∨ ¯5 5")
    2.5 2.5
    >>> test(r"¯7.5 ∨ ¯5 5")
    2.5 2.5
    """
    pass

# --------------

def     and_lcm():
    """
    >>> test(r"0 ∧ 0 1")
    0 0
    >>> test(r"1 ∧ 0 1")
    0 1

    >>> test(r"TEN ← 1 2 3 4 5 6 7 8 9 10")
    1 2 3 4 5 6 7 8 9 10

    >>> test(r"(TEN) ∧ 10")
    10 10 30 20 10 30 70 40 90 10
    >>> test(r"(-TEN) ∧ 10")
    ¯10 ¯10 ¯30 ¯20 ¯10 ¯30 ¯70 ¯40 ¯90 ¯10
    >>> test(r"(TEN) ∧ ¯10")
    ¯10 ¯10 ¯30 ¯20 ¯10 ¯30 ¯70 ¯40 ¯90 ¯10
    >>> test(r"(-TEN) ∧ ¯10")
    10 10 30 20 10 30 70 40 90 10

    >>> test(r"7.5 ∧ ¯5 5")
    ¯15 15
    >>> test(r"¯7.5 ∧ ¯5 5")
    15 ¯15
    """
    pass

# --------------

def     nor():
    """
    >>> test(r"0 ⍱ ¯1")
    DOMAIN ERROR
    >>> test(r"¯1 ⍱ 0")
    DOMAIN ERROR

    >>> test(r"0 ⍱ 0 1")
    1 0
    >>> test(r"1 ⍱ 0 1")
    0 0

    >>> test(r"0.5 ⍱ 0")
    DOMAIN ERROR
    >>> test(r"1 ⍱ 0.5")
    DOMAIN ERROR
    """
    pass

# --------------

def     nand():
    """
    >>> test(r"0 ⍲ ¯1")
    DOMAIN ERROR
    >>> test(r"¯1 ⍲ 0")
    DOMAIN ERROR

    >>> test(r"0 ⍲ 0 1")
    1 1
    >>> test(r"1 ⍲ 0 1")
    1 0

    >>> test(r"0.5 ⍲ 0")
    DOMAIN ERROR
    >>> test(r"1 ⍲ 0.5")
    DOMAIN ERROR
    """
    pass

# ------------------------------

def     lt():
    """
    >>> test(r"AC ← ¯0.5 ¯0.5 0.5 0.5")
    ¯0.5 ¯0.5 0.5 0.5
    >>> test(r"BC ← ¯0.5 0.5 ¯0.5 0.5")
    ¯0.5 0.5 ¯0.5 0.5

    >>> test(r"AC < BC")
    0 1 0 0

    >>> test(r"AC ← AC + ⎕CT")
    ¯0.5 ¯0.5 0.5 0.5
    >>> test(r"BC ← BC - ⎕CT")
    ¯0.5 0.5 ¯0.5 0.5

    >>> test(r"AC < BC")
    0 1 0 0

    >>> test(r"AC ← AC + 10")
    9.5 9.5 10.5 10.5
    >>> test(r"BC ← BC + 10")
    9.5 10.5 9.5 10.5

    >>> test(r"AC < BC")
    0 1 0 0
    """
    pass

# --------------

def     le():
    """
    >>> test(r"AC ← ¯0.5 ¯0.5 0.5 0.5")
    ¯0.5 ¯0.5 0.5 0.5
    >>> test(r"BC ← ¯0.5 0.5 ¯0.5 0.5")
    ¯0.5 0.5 ¯0.5 0.5

    >>> test(r"AC ≤ BC")
    1 1 0 1

    >>> test(r"AC ← AC + ⎕CT")
    ¯0.5 ¯0.5 0.5 0.5
    >>> test(r"BC ← BC - ⎕CT")
    ¯0.5 0.5 ¯0.5 0.5

    >>> test(r"AC ≤ BC")
    0 1 0 0

    >>> test(r"AC ← AC + 10")
    9.5 9.5 10.5 10.5
    >>> test(r"BC ← BC + 10")
    9.5 10.5 9.5 10.5

    >>> test(r"AC ≤ BC")
    1 1 0 1
    """
    pass

# --------------

def     ge():
    """
    >>> test(r"AC ← ¯0.5 ¯0.5 0.5 0.5")
    ¯0.5 ¯0.5 0.5 0.5
    >>> test(r"BC ← ¯0.5 0.5 ¯0.5 0.5")
    ¯0.5 0.5 ¯0.5 0.5

    >>> test(r"AC ≥ BC")
    1 0 1 1

    >>> test(r"AC ← AC + ⎕CT")
    ¯0.5 ¯0.5 0.5 0.5
    >>> test(r"BC ← BC - ⎕CT")
    ¯0.5 0.5 ¯0.5 0.5

    >>> test(r"AC ≥ BC")
    1 0 1 1

    >>> test(r"AC ← AC + 10")
    9.5 9.5 10.5 10.5
    >>> test(r"BC ← BC + 10")
    9.5 10.5 9.5 10.5

    >>> test(r"AC ≥ BC")
    1 0 1 1
    """
    pass

# --------------


def     gt():
    """
    >>> test(r"AC ← ¯0.5 ¯0.5 0.5 0.5")
    ¯0.5 ¯0.5 0.5 0.5
    >>> test(r"BC ← ¯0.5 0.5 ¯0.5 0.5")
    ¯0.5 0.5 ¯0.5 0.5

    >>> test(r"AC > BC")
    0 0 1 0

    >>> test(r"AC ← AC + ⎕CT")
    ¯0.5 ¯0.5 0.5 0.5
    >>> test(r"BC ← BC - ⎕CT")
    ¯0.5 0.5 ¯0.5 0.5

    >>> test(r"AC > BC")
    1 0 1 1

    >>> test(r"AC ← AC + 10")
    9.5 9.5 10.5 10.5
    >>> test(r"BC ← BC + 10")
    9.5 10.5 9.5 10.5

    >>> test(r"AC > BC")
    0 0 1 0
    """
    pass

# --------------

def     eq():
    """
    >>> test(r"AC ← ¯0.5 ¯0.5 0.5 0.5")
    ¯0.5 ¯0.5 0.5 0.5
    >>> test(r"BC ← ¯0.5 0.5 ¯0.5 0.5")
    ¯0.5 0.5 ¯0.5 0.5

    >>> test(r"AC = BC")
    1 0 0 1

    >>> test(r"AC ← AC + ⎕CT")
    ¯0.5 ¯0.5 0.5 0.5
    >>> test(r"BC ← BC - ⎕CT")
    ¯0.5 0.5 ¯0.5 0.5

    >>> test(r"AC = BC")
    0 0 0 0

    >>> test(r"AC ← AC + 10")
    9.5 9.5 10.5 10.5
    >>> test(r"BC ← BC + 10")
    9.5 10.5 9.5 10.5

    >>> test(r"AC = BC")
    1 0 0 1
    """
    pass

# --------------

def     ne():
    """
    >>> test(r"AC ← ¯0.5 ¯0.5 0.5 0.5")
    ¯0.5 ¯0.5 0.5 0.5
    >>> test(r"BC ← ¯0.5 0.5 ¯0.5 0.5")
    ¯0.5 0.5 ¯0.5 0.5

    >>> test(r"AC ≠ BC")
    0 1 1 0

    >>> test(r"AC ← AC + ⎕CT")
    ¯0.5 ¯0.5 0.5 0.5
    >>> test(r"BC ← BC - ⎕CT")
    ¯0.5 0.5 ¯0.5 0.5

    >>> test(r"AC ≠ BC")
    1 1 1 1

    >>> test(r"AC ← AC + 10")
    9.5 9.5 10.5 10.5
    >>> test(r"BC ← BC + 10")
    9.5 10.5 9.5 10.5

    >>> test(r"AC ≠ BC")
    0 1 1 0
    """
    pass

# ------------------------------

def     depth_match():
    """
    >>> test(r"1.2 ≡ 1.2")
    1
    >>> test(r"1.2 ≡ 2.1")
    0
    >>> test(r"1.2 ≡ ,1.2")
    0

    >>> test(r"⍴ 1.2 ≡ 1.2")
    ⍬
    >>> test(r"⍴ 1.2 ≡ ,1.2")
    ⍬

    >>> test(r"1 ≡ 1 2 3")
    0
    >>> test(r"1 2 ≡ 1 2 3")
    0
    >>> test(r"1 2 3 ≡ 1 2 3")
    1
    >>> test(r"1 2 3 ≡ 1 2")
    0
    >>> test(r"1 2 3 ≡ 1")
    0

    >>> IO = saveIndexOrigin()
    >>> setIndexOrigin(1)
    >>> test(r"1 2 3 ≡ ⍳ 3")
    1
    >>> test(r"2 3 1 ≡ ⍳ 3")
    0
    >>> test(r"3 1 2 ≡ ⍳ 3")
    0
    >>> restoreIndexOrigin(IO)
    """
    pass

# --------------

def     tally_notMatch():
    """
    >>> test(r"1.2 ≢ 1.2")
    0
    >>> test(r"1.2 ≢ 2.1")
    1
    >>> test(r"1.2 ≢ ,1.2")
    1

    >>> test(r"⍴ 1.2 ≢ 1.2")
    ⍬
    >>> test(r"⍴ 1.2 ≢ ,1.2")
    ⍬

    >>> test(r"1 ≢ 1 2 3")
    1
    >>> test(r"1 2 ≢ 1 2 3")
    1
    >>> test(r"1 2 3 ≢ 1 2 3")
    0
    >>> test(r"1 2 3 ≢ 1 2")
    1
    >>> test(r"1 2 3 ≢ 1")
    1

    >>> IO = saveIndexOrigin()
    >>> setIndexOrigin(1)
    >>> test(r"1 2 3 ≢ ⍳ 3")
    0
    >>> test(r"2 3 1 ≢ ⍳ 3")
    1
    >>> test(r"3 1 2 ≢ ⍳ 3")
    1
    >>> restoreIndexOrigin(IO)
    """
    pass

# ------------------------------

def     rho():
    """
    >>> test(r"1.2 ⍴ 1.2")
    DOMAIN ERROR

    >>> test(r"1 ⍴ 1.2")
    1.2

    >>> test(r"⍴ 1 ⍴ 1.2")
    1
    >>> test(r"⍴ 1 ⍴ ,1.2")
    1

    >>> test(r"2 ⍴ 1.2")
    1.2 1.2
    >>> test(r"⍴ 2 ⍴ 1.2")
    2

    >>> test(r"8 ⍴ 1 2 3 4")
    1 2 3 4 1 2 3 4
    >>> test(r"8 ⍴ 1 2 3 4 5 6 7 8")
    1 2 3 4 5 6 7 8
    >>> test(r"8 ⍴ 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16")
    1 2 3 4 5 6 7 8

    >>> test(r"3 ⍴ 1 2 3 4")
    1 2 3
    >>> test(r"4 ⍴ 1 2 3 4")
    1 2 3 4
    >>> test(r"5 ⍴ 1 2 3 4")
    1 2 3 4 1

    >>> test(r"1 2 ⍴ 1 2")
    WIP - MATRIX ERROR

    >>> test(r"15 ⍴ 0 + 1 2 3 4 5 6")
    1 2 3 4 5 6 1 2 3 4 5 6 1 2 3
    """
    pass

# --------------

def     comma():
    """
    >>> test(r"1.2 , 1.2")
    1.2 1.2
    >>> test(r"⍴ 1.2 , 1.2")
    2

    >>> test(r"0 1, 2")
    0 1 2
    >>> test(r"0, 1 2")
    0 1 2
    >>> test(r"0 1, 2 3")
    0 1 2 3

    >>> test(r"⍴ 0 1, 2")
    3
    >>> test(r"⍴ 0, 1 2")
    3
    >>> test(r"⍴ 0 1, 2 3")
    4
    """
    pass

# --------------

def     enlist_membership():
    """
    >>> test(r"1.2 ∊ 1.2")
    1
    >>> test(r"2.1 ∊ 1.2")
    0

    >>> test(r"⍴ 1.2 ∊ 1.2")
    ⍬
    >>> test(r"⍴ 2.1 ∊ 1.2")
    ⍬

    >>> test(r"3 1 4 ∊ 1 3 5 7 9")
    1 1 0
    >>> test(r"3 1 4 ∊ 0 2 4 6 8")
    0 0 1

    >>> test(r"⍴ 3 1 4 ∊ 1 3 5 7 9")
    3
    >>> test(r"⍴ 3 1 4 ∊ 0 2 4 6 8")
    3
    """
    pass

# --------------

def     find():
    """
    only dyadic

    >>> test(r"1.2 ⍷ 1.2")
    1
    >>> test(r"2.1 ⍷ 1.2")
    0

    >>> test(r"⍴ 1.2 ⍷ 1.2")
    ⍬
    >>> test(r"⍴ 2.1 ⍷ 1.2")
    ⍬

    >>> test(r"3 1 4 ⍷ 1 3 5 7 9")
    0 0 0 0 0
    >>> test(r"3 1 4 ⍷ 0 3 1 4 8")
    0 1 0 0 0

    >>> test(r"⍴ 3 1 4 ⍷ 1 3 5 7 9")
    5
    >>> test(r"⍴ 3 1 4 ⍷ 0 2 4 6 8")
    5

    >>> test(r"3 4 ⍷ 1 2 3 4")
    0 0 1 0
    >>> test(r"3 4 ⍷ 2 3 4 5")
    0 1 0 0
    >>> test(r"3 4 ⍷ 3 4 5 6")
    1 0 0 0

    >>> test(r"4 4 ⍷ 1 2 3 4")
    0 0 0 0
    >>> test(r"4 4 ⍷ 1 2 4 4")
    0 0 1 0
    >>> test(r"4 4 ⍷ 4 2 4 4")
    0 0 1 0
    >>> test(r"4 4 ⍷ 4 4 4 4")
    1 1 1 0
    """
    pass

# --------------

def     transpose():
    """
    >>> test(r"1.2 ⍉ 1.2")
    LENGTH ERROR
    >>> test(r"1.2 ⍉ ,1.2")
    DOMAIN ERROR

    >>> test(r"1 ⍉ 1.2")
    LENGTH ERROR
    >>> test(r"1 ⍉ ,1.2")
    1.2

    >>> test(r"⍴ 1 ⍉ ,1.2")
    1

    >>> test(r"1 ⍉ 1 2 3")
    1 2 3
    >>> test(r"2 ⍉ 1 2 3")
    DOMAIN ERROR
    >>> test(r"0 ⍉ 1 2 3")
    DOMAIN ERROR
    >>> test(r"1.2 ⍉ 1 2 3")
    DOMAIN ERROR

    >>> test(r"1 1 ⍉ 1 2 3")
    LENGTH ERROR
    >>> test(r"1 2 3 ⍉ 1 2 3")
    LENGTH ERROR
    """
    pass

# --------------

def     reverse_rotate():
    """
    >>> test(r"1.2 ⌽ 1.2")
    DOMAIN ERROR
    >>> test(r"1.2 ⌽ ,1.2")
    DOMAIN ERROR

    >>> test(r"1 ⌽ 1.2")
    1.2

    >>> test(r"⍴ 1 ⌽ 1.2")
    ⍬
    >>> test(r"⍴ 1 ⌽ ,1.2")
    1

    >>> test(r"101 ⌽ 1.2")
    1.2

    >>> test(r"1 ⌽ 1 2 3 4 5 6")
    2 3 4 5 6 1
    >>> test(r"2 ⌽ 1 2 3 4 5 6")
    3 4 5 6 1 2

    >>> test(r"¯1 ⌽ 1 2 3 4 5 6")
    6 1 2 3 4 5
    >>> test(r"¯2 ⌽ 1 2 3 4 5 6")
    5 6 1 2 3 4

    >>> test(r"6 ⌽ 1 2 3 4 5 6")
    1 2 3 4 5 6
    >>> test(r"0 ⌽ 1 2 3 4 5 6")
    1 2 3 4 5 6
    >>> test(r"¯6 ⌽ 1 2 3 4 5 6")
    1 2 3 4 5 6

    >>> test(r"7 ⌽ 1 2 3 4 5 6")
    2 3 4 5 6 1
    >>> test(r"¯7 ⌽ 1 2 3 4 5 6")
    6 1 2 3 4 5

    >>> test(r"1 2 ⌽ 1 2 3 4 5 6")
    RANK ERROR
    >>> test(r"1.2 ⌽ 1 2 3 4 5 6")
    DOMAIN ERROR
    """
    pass

# --------------

def     enclose_partition():
    """
    >>> test(r"1 ⊂ 1")
    RANK ERROR
    >>> test(r"1 ⊂ ,1")
    (1)
    >>> test(r"⍴ 1 ⊂ ,1")
    ⍬
    >>> test(r"≡ 1 ⊂ ,1")
    2

    >>> test(r"1 2 3 ⊂ 11 22 33")
    (11) (22) (33)
    >>> test(r"3 2 1 ⊂ 11 22 33")
    (11 22 33)

    >>> test(r"1 2 2 3 3 3 ⊂ 11 21 22 31 32 33")
    (11) (21 22) (31 32 33)
    >>> test(r"1 1 1 2 2 3 ⊂ 11 21 22 31 32 33")
    (11 21 22) (31 32) (33)

    >>> test(r"1 2 2 3 0 3 ⊂ 11 21 22 31 32 33")
    (11) (21 22) (31) (33)

    >>> test(r"0 2 2 3 0 3 ⊂ 11 21 22 31 32 33")
    (21 22) (31) (33)
    >>> test(r"0 2 2 3 0 0 ⊂ 11 21 22 31 32 33")
    (21 22) (31)

    >>> test(r"0 2 2 3 0 0 3 ⊂ 11 21 22 31 32 33", True)
    LENGTH ERROR
    >>> test(r"0 2 2 3 0 0 ⊂ 11 21 22 31 32 33 41", True)
    LENGTH ERROR
    """
    pass

# --------------

def     disclose_pick():
    """
    >>> IO = saveIndexOrigin()
    >>> setIndexOrigin(1)

    >>> test(r"1 ⊃ 10")
    RANK ERROR
    >>> test(r"1 ⊃ ,10")
    10
    >>> test(r"1.2 ⊃ ,10")
    DOMAIN ERROR

    >>> test(r"0 ⊃ 10 20 30")
    INDEX ERROR
    >>> test(r"1 ⊃ 10 20 30")
    10
    >>> test(r"2 ⊃ 10 20 30")
    20
    >>> test(r"3 ⊃ 10 20 30")
    30
    >>> test(r"4 ⊃ 10 20 30")
    INDEX ERROR

    >>> setIndexOrigin(0)

    >>> test(r"¯1 ⊃ 10 20 30")
    INDEX ERROR
    >>> test(r"0 ⊃ 10 20 30")
    10
    >>> test(r"1 ⊃ 10 20 30")
    20
    >>> test(r"2 ⊃ 10 20 30")
    30
    >>> test(r"3 ⊃ 10 20 30")
    INDEX ERROR

    >>> restoreIndexOrigin(IO)
    """
    pass

# ------------------------------

def     iota():
    """
    >>> IO = saveIndexOrigin()
    >>> setIndexOrigin(1)

    >>> test(r"1.2 ⍳ 1.2")
    1

    >>> test(r"⍴ 1 ⍳ 1.2")
    ⍬
    >>> test(r"⍴ 1 ⍳ ,1.2")
    1

    >>> test(r"1 ⍳ 1")
    1
    >>> test(r"1 ⍳ 0")
    2

    >>> test(r"1 5 2 4 3 ⍳ 2")
    3
    >>> test(r"1 5 2 4 3 ⍳ 1 2 3 4 5")
    1 3 5 4 2

    >>> test(r"2 2 2 2 2 ⍳ 2 2")
    1 1
    >>> test(r"2 2 2 2 2 ⍳ 3 6 9")
    6 6 6

    >>> setIndexOrigin(0)

    >>> test(r"1.2 ⍳ 1.2")
    0

    >>> test(r"⍴ 1 ⍳ 1.2")
    ⍬
    >>> test(r"⍴ 1 ⍳ ,1.2")
    1

    >>> test(r"1 ⍳ 1")
    0
    >>> test(r"1 ⍳ 0")
    1

    >>> test(r"1 5 2 4 3 ⍳ 2")
    2
    >>> test(r"1 5 2 4 3 ⍳ 1 2 3 4 5")
    0 2 4 3 1

    >>> test(r"2 2 2 2 2 ⍳ 2 2")
    0 0
    >>> test(r"2 2 2 2 2 ⍳ 3 6 9")
    5 5 5

    >>> restoreIndexOrigin(IO)
    """
    pass

# --------------

def     tilde():
    """
    >>> test(r"1 ~ 1")
    ⍬
    >>> test(r"1 ~ 0")
    1

    >>> test(r"10 ~ 1.2")
    10

    >>> test(r"⍴ 10 ~ 1.2")
    1
    >>> test(r"⍴ 10 ~ ,1.2")
    1

    >>> test(r"1 5 2 4 3 ~ ⍬")
    1 5 2 4 3
    >>> test(r"1 5 2 4 3 ~ 2")
    1 5 4 3
    >>> test(r"1 5 2 4 3 ~ 2 2")
    1 5 4 3

    >>> test(r"1 2 3 4 5 ~ 5 4 3 2 1")
    ⍬
    >>> test(r"2 2 2 2 2 ~ 2 2")
    ⍬
    >>> test(r"2 2 2 2 2 ~ 3 6 9")
    2 2 2 2 2
    """
    pass

# --------------

def     unique_union():
    """
    >>> test(r"1.2 ∪ 1.2")
    1.2
    >>> test(r"1.2 ∪ ,1.2")
    1.2

    >>> test(r"⍴ 1.2 ∪ 1.2")
    1
    >>> test(r"⍴ 1.2 ∪ ,1.2")
    1

    >>> test(r"1 2 3 ∪ 6 5 4")
    1 2 3 6 5 4
    >>> test(r"1 2 3 ∪ 3 2 1")
    1 2 3

    >>> test(r"1 1 1 ∪ 1")
    1 1 1
    >>> test(r"1 ∪ 1 1 1")
    1
    """
    pass

# --------------

def     intersection():
    """
    >>> test(r"1.2 ∩ 1.2")
    1.2
    >>> test(r"1.2 ∩ ,1.2")
    1.2

    >>> test(r"⍴ 1.2 ∩ 1.2")
    1
    >>> test(r"⍴ 1.2 ∩ ,1.2")
    1

    >>> test(r"1 2 3 ∩ 6 5 4")
    ⍬
    >>> test(r"1 2 3 ∩ 3 2 1")
    1 2 3

    >>> test(r"1 1 1 ∩ 1")
    1 1 1
    >>> test(r"1 ∩ 1 1 1")
    1
    """
    pass

# --------------

def     tail_drop():
    """
    >>> test(r"1 ↓ 1.2")
    ⍬
    >>> test(r"1 ↓ ,1.2")
    ⍬

    >>> test(r"⍴ 1 ↓ 1.2")
    0
    >>> test(r"⍴ 1 ↓ ,1.2")
    0

    >>> test(r"3 ↓ 1 2 3 4 5 6")
    4 5 6
    >>> test(r"¯3 ↓ 1 2 3 4 5 6")
    1 2 3
    >>> test(r"0 ↓ 1 2 3 4 5 6")
    1 2 3 4 5 6

    >>> test(r"3.3 ↓ 1 2 3 4 5 6")
    DOMAIN ERROR
    >>> test(r"3 3 ↓ 1 2 3 4 5 6")
    LENGTH ERROR
    """
    pass

# --------------

def     head_take():
    """
    >>> test(r"3 ↑ 1 2 3 4 5 6")
    1 2 3
    >>> test(r"¯3 ↑ 1 2 3 4 5 6")
    4 5 6
    >>> test(r"0 ↑ 1 2 3 4 5 6")
    ⍬

    >>> test(r"3 ↑ 1 2 3")
    1 2 3
    >>> test(r"¯3 ↑ 1 2 3")
    1 2 3
    >>> test(r"6 ↑ 1 2 3")
    1 2 3 0 0 0
    >>> test(r"¯6 ↑ 1 2 3")
    0 0 0 1 2 3

    >>> test(r"3.3 ↑ 1 2 3 4 5 6")
    DOMAIN ERROR
    >>> test(r"3 3 ↑ 1 2 3 4 5 6")
    LENGTH ERROR
    """
    pass

# --------------

def     compress_replicate():
    """
    >>> test(r"1 1 1 / 1 2 3")
    1 2 3
    >>> test(r"1 1 / 1 2 3", True)
    LENGTH ERROR
    >>> test(r"1 1 1 1 / 1 2 3", True)
    LENGTH ERROR
    >>> test(r"1 0 1 / 1 2 3")
    1 3

    >>> test(r"1 2 3 / 1 2 3")
    1 2 2 3 3 3
    >>> test(r"1 ¯2 3 / 1 2 3")
    1 0 0 3 3 3

    >>> test(r"0 / 1 2 3")
    ⍬
    >>> test(r"1 / 1 2 3")
    1 2 3
    >>> test(r"¯1 / 1 2 3")
    0 0 0
    """
    pass

# --------------

def     expand():
    """
    >>> test(r"1 1 1 \\ 1 2 3")
    1 2 3
    >>> test(r"1 1 \\ 1 2 3", True)
    LENGTH ERROR
    >>> test(r"1 1 1 1 \\ 1 2 3", True)
    LENGTH ERROR

    >>> test(r"1 0 1 0 1 \\ 1 2 3")
    1 0 2 0 3
    >>> test(r"1 0 1 0 1 0 0 0 1 \\ 1 2 3", True)
    LENGTH ERROR
    >>> test(r"1 0 2 0 3 \\ 1 2 3")
    1 0 2 2 0 3 3 3
    >>> test(r"1 0 2 0 0 \\ 1 2 3", True)
    LENGTH ERROR

    >>> test(r"¯1 1 ¯2 1 ¯3 1 0 \\ 1 2 3")
    0 1 0 0 2 0 0 0 3 0

    >>> test(r"0 \\ 1 2 3")
    0
    >>> test(r"1 \\ 1 2 3")
    1 2 3
    >>> test(r"¯1 \\1 2 3")
    LENGTH ERROR
    """
    pass

# ------------------------------

def     encode():
    """
    >>> test(r"16 16 ⊤ 17")
    1 1
    >>> test(r"16 8 ⊤ 17")
    2 1
    >>> test(r"16 16 8 ⊤ 17")
    0 2 1
    >>> test(r"8 ⊤ 17")
    1

    >>> test(r"16 8 ⊤ 256 + 17")
    2 1
    >>> test(r"16 16 8 ⊤ 256 + 17")
    2 2 1
    >>> test(r"16 0 8 ⊤ 256 + 17")
    0 34 1

    >>> test(r"0 1 ⊤ ○ 1")
    3 0.1415926536
    >>> test(r"8.5 8.5 ⊤ 17")
    2 0
    """
    pass

# --------------

def     decode():
    """
    >>> test(r"16 16 ⊥ 1 1")
    17
    >>> test(r"16 8 ⊥ 2 1")
    17
    >>> test(r"16 16 8 ⊥ 2 1")
    LENGTH ERROR

    >>> test(r"8 ⊥ 2 1")
    17
    >>> test(r"8 ⊥ 1")
    1
    >>> test(r"8 8 ⊥ 1")
    9

    >>> test(r"16 16 8 ⊥ 1 2 1")
    145
    >>> test(r"16 0 8 ⊥ 0 34 1")
    273

    >>> test(r"0 1 ⊥ 3 0.14159265436")
    3.141592654
    >>> test(r"8.5 8.5 ⊥ 2 0")
    17
    """
    pass

# --------------

def     gradeUp():
    """
    >>> IO = saveIndexOrigin()
    >>> setIndexOrigin(1)

    >>> test(r"1 2 3 ⍋ 1 2 3")
    DOMAIN ERROR
    >>> test(r"'xcybza' ⍋ 1 2 3")
    DOMAIN ERROR
    >>> test(r"1 2 3 ⍋ 'xcybza'")
    DOMAIN ERROR

    >>> setIndexOrigin(0)

    >>> test(r"1 2 3 ⍋ 1 2 3")
    DOMAIN ERROR
    >>> test(r"'xcybza' ⍋ 1 2 3")
    DOMAIN ERROR
    >>> test(r"1 2 3 ⍋ 'xcybza'")
    DOMAIN ERROR

    >>> restoreIndexOrigin(IO)
    """
    pass

# --------------

def     gradeDown():
    """
    >>> IO = saveIndexOrigin()
    >>> setIndexOrigin(1)

    >>> test(r"1 2 3 ⍒ 1 2 3")
    DOMAIN ERROR
    >>> test(r"'xcybza' ⍒ 1 2 3")
    DOMAIN ERROR
    >>> test(r"1 2 3 ⍒ 'xcybza'")
    DOMAIN ERROR

    >>> setIndexOrigin(0)

    >>> test(r"1 2 3 ⍒ 1 2 3")
    DOMAIN ERROR
    >>> test(r"'xcybza' ⍒ 1 2 3")
    DOMAIN ERROR
    >>> test(r"1 2 3 ⍒ 'xcybza'")
    DOMAIN ERROR

    >>> restoreIndexOrigin(IO)
    """
    pass

# ------------------------------

if __name__ == "__main__":
    preamble()
    if test and __name__:
        import doctest
        doctest.testmod()
    else:
        IO = saveIndexOrigin()
        setIndexOrigin(0)
        restoreIndexOrigin(IO)

# EOF
