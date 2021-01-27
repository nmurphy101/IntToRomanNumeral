#!/usr/bin/env python3

"""
    Converter
    ~~~~~~~~~~

    Takes an input and converts it to any number
    of potential options.

    Current Options:
     - Integer to Roman Numeral

    :copyright: (c) 2021 by Nicholas Murphy.
    :license: GPLv2, see LICENSE for more details.
"""

from abc import ABC, abstractmethod

class Converter(ABC):
    """
    Converter
    ~~~~~~~~~~

    Abstract class object for a baseline Converter.
    """
    def __init__(self, number):
        super(Converter, self).__init__()
        # Inputted number to be converted
        self.number = number
        # Result value
        self.result = None

    @abstractmethod
    def convert(self):
        """
        convert
        ~~~~~~~~~~

        Abstract method for new subclasses to overide for their own conversion.
        """

class Roman(Converter):
    """
    Roman
    ~~~~~~~~~~

    A roman numeral converter.
    """
    def __init__(self, number):
        super(Roman, self).__init__(number)
        # Run the conversion
        self.convert()

    def convert(self):
        """
        convert
        ~~~~~~~~~~

        Takes an integer and converts it to it's equivilant string
        of roman numerals, and sets the result.
        """
        # Make sure the user input is an integer between 0 and 4000
        integer = int(self.number)
        if not 1 <= integer <= 3999:
            raise ValueError("Enter a valid integer between 0 and 4000")

        # Symbol with it's respective integer place
        roman_numeral_table = [
            ("M", 1000), ("CM", 900), ("D", 500),
            ("CD", 400), ("C", 100), ("XC", 90),
            ("L", 50), ("XL", 40), ("X", 10),
            ("IX", 9), ("V", 5), ("IV", 4),
            ("I", 1)
        ]
        # Initilize the numeral list
        roman_numerals = []
        # Loop over the roman numeral table
        for numeral, value in roman_numeral_table:
            # Get the quotent and remainder from a %mod calculation
            count, integer = divmod(integer, value)
            # Add the resulting numerals to the final result list
            roman_numerals.append(numeral * count)
        # Join the final result (which is faster than str concatenation) into a str
        self.result = ''.join(roman_numerals)

def main():
    '''
    main
    ~~~~~~~~~~

    Example usage when this file is run directly
    '''
    # Get user input with a prompt
    user_input = input("Please input a integer between 0 and 3999: ")
    # Show the results
    print("Result is: ", Roman(user_input).result)

if __name__ == "__main__":
    main()
