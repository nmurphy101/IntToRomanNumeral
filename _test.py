#!/usr/bin/env python3

"""
    Pytest file
    ~~~~~~~~~~

    Utilizes pytest to test project code
"""

import pytest
from .converter import Roman


def test_roman_str_input():
    """
    Makes sure string inputs work
    """
    converter = Roman("3594")
    converter.convert()
    assert converter.result == "MMMDXCIV"

def test_roman_int_input():
    """
    Makes sure integer inputs work
    """
    converter = Roman(3594)
    converter.convert()
    assert converter.result == "MMMDXCIV"

def test_roman_raises_exception_on_non_int_values():
    """
    Makes sure inputs that are not integer values raises an error
    """
    with pytest.raises(ValueError):
        converter = Roman("g")
        converter.convert()

def test_roman_raises_exception_on_wrong_low_int_values():
    """
    Makes sure inputs that are too low integer values raises an error
    """
    with pytest.raises(ValueError):
        converter = Roman("0")
        converter.convert()

def test_roman_raises_exception_on_wrong_high_int_values():
    """
    Makes sure inputs that are too high integer values raises an error
    """
    with pytest.raises(ValueError):
        converter = Roman("4000")
        converter.convert()

def test_roman_succeeds_on_correct_values_ones():
    """
    Makes sure inputs that are within the requirements range succeed
    """
    for test_val in range(1, 10):
        converter = Roman(test_val)
        converter.convert()

def test_roman_succeeds_on_correct_values_tens():
    """
    Makes sure inputs that are within the requirements range succeed
    """
    for test_val in range(10, 100):
        converter = Roman(test_val)
        converter.convert()

def test_roman_succeeds_on_correct_values_hundreds():
    """
    Makes sure inputs that are within the requirements range succeed
    """
    for test_val in range(100, 1000):
        converter = Roman(test_val)
        converter.convert()

def test_roman_succeeds_on_correct_values_thousands():
    """
    Makes sure inputs that are within the requirements range succeed
    """
    for test_val in range(1000, 3999):
        converter = Roman(test_val)
        converter.convert()
