#!/usr/bin/env python3

"""
    Pytest file
    ~~~~~~~~~~

    Utilizes pytest to test project code
"""

import pytest
from .converter import Roman


# Roman convert function section
def test_roman_convert_str_input():
    """
    Makes sure string inputs work
    """
    converter = Roman("3594")
    converter.convert()
    assert converter.result == "MMMDXCIV"

def test_roman_convert_int_input():
    """
    Makes sure integer inputs work
    """
    converter = Roman(3594)
    converter.convert()
    assert converter.result == "MMMDXCIV"

def test_roman_convert_raises_exception_on_non_int_values():
    """
    Makes sure inputs that are not integer values raises an error
    """
    with pytest.raises(ValueError):
        converter = Roman("g")
        converter.convert()

def test_roman_convert_raises_exception_on_wrong_low_int_values():
    """
    Makes sure inputs that are too low integer values raises an error
    """
    with pytest.raises(ValueError):
        converter = Roman("0")
        converter.convert()

def test_roman_convert_raises_exception_on_wrong_high_int_values():
    """
    Makes sure inputs that are too high integer values raises an error
    """
    with pytest.raises(ValueError):
        converter = Roman("4000")
        converter.convert()

def test_roman_convert_succeeds_on_correct_values_ones():
    """
    Makes sure inputs that are within the requirements range succeed
    """
    for test_val in range(1, 10):
        converter = Roman(test_val)
        converter.convert()

def test_roman_convert_succeeds_on_correct_values_tens():
    """
    Makes sure inputs that are within the requirements range succeed
    """
    for test_val in range(10, 100):
        converter = Roman(test_val)
        converter.convert()

def test_roman_convert_succeeds_on_correct_values_hundreds():
    """
    Makes sure inputs that are within the requirements range succeed
    """
    for test_val in range(100, 1000):
        converter = Roman(test_val)
        converter.convert()

def test_roman_convert_succeeds_on_correct_values_thousands():
    """
    Makes sure inputs that are within the requirements range succeed
    """
    for test_val in range(1000, 3999):
        converter = Roman(test_val)
        converter.convert()


# Roman deconvert function section
def test_roman_deconvert_str_input():
    """
    Makes sure string inputs work
    """
    converter = Roman("MMCCCXLV")
    converter.deconvert()
    assert converter.result == 2345

def test_roman_deconvert_raises_exception_on_non_str_values():
    """
    Makes sure inputs that are not integer values raises an error
    """
    with pytest.raises(TypeError):
        converter = Roman(42)
        converter.deconvert()

def test_roman_deconvert_lowest_input():
    """
    Makes sure string inputs work
    """
    converter = Roman("I")
    converter.deconvert()
    assert converter.result == 1

def test_roman_deconvert_highest_input():
    """
    Makes sure string inputs work
    """
    converter = Roman("MMMCMXCIX")
    converter.deconvert()
    assert converter.result == 3999

def test_roman_deconvert_raises_exception_on_wrong_high_roman_numeral_values():
    """
    Makes sure inputs that are too high roman numeral values raises an error
    """
    with pytest.raises(ValueError):
        converter = Roman("MMMM")
        converter.deconvert()