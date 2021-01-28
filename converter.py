#!/usr/bin/env python3

"""
    Converter
    ~~~~~~~~~~

    Takes an input and converts it to any number
    of potential options.

    Current Options:
     - Integer to Roman Numeral & Roman Numeral to Integer

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
    
    def __init__(self, value):
        super(Converter, self).__init__()
        # Inputted value to be converted
        self.value = value
        # Resulting converted value
        self.result = None

    @abstractmethod
    def convert(self):
        """
        convert
        ~~~~~~~~~~

        Abstract convert method for new subclasses to overide for their own conversion.
        """
    
    @abstractmethod
    def deconvert(self):
        """
        deconvert
        ~~~~~~~~~~

        Abstract deconvert method for new subclasses to overide for their own deconversion.
        """


class Roman(Converter):
    """
    Roman
    ~~~~~~~~~~

    A roman numeral converter.
    """

    def __init__(self, value):
        super(Roman, self).__init__(value)
        # Roman numerals with their respective value
        self.roman_numeral_table = [
                ("M", 1000), ("CM", 900), ("D", 500),
                ("CD", 400), ("C", 100), ("XC", 90),
                ("L", 50), ("XL", 40), ("X", 10),
                ("IX", 9), ("V", 5), ("IV", 4),
                ("I", 1)
            ]

    def convert(self):
        """
        convert
        ~~~~~~~~~~

        Takes an integer and converts it to it's equivilant string
        of roman numerals, and sets the result.
        """

        # Make sure the user input is an integer between 0 and 4000
        integer = int(self.value)
        if not 1 <= integer <= 3999:
            raise ValueError("Enter a valid integer between 0 and 4000")

        # Initilize the numeral list
        roman_numerals = []

        # Exit when integer reaches 0
        while integer:
            # Loop over the roman numeral table
            for numeral, value in self.roman_numeral_table:
                # Get the quotent and remainder from a %mod calculation
                count, integer = divmod(integer, value)
                # Add the resulting numerals to the final result list
                roman_numerals.append(numeral * count)
        
        # Join the final result (which is faster than str concatenation) into a str
        self.result = ''.join(roman_numerals)

    def deconvert(self):
        """
        deconvert
        ~~~~~~~~~~

        Takes a roman numeral str and deconverts it to it's equivilant
        integer, and sets the result.
        """

        # Make sure the user input is a roman numeral string
        usr_str = str(self.value).upper()
        if not any(i in "IVXLCDM" for i in usr_str):
            raise TypeError("Only enter valid roman numeral characters")
        
        # Internal result int to replace class result var
        result = 0
        
        # Flag for if a double roman numeral is found
        double_found = False

        # Loop through each character in usr_str
        for index, char in enumerate(usr_str):
            # If a double character was found
            if double_found == True:
                # Reset the flag
                double_found = False
                # Skip this character (as it was part of the 'double')
                continue

            # Initilize/reset the holding integer
            holding_val = 0

            # Loop over the roman numeral table
            for numeral, value in self.roman_numeral_table:
                # Check for a two character roman numeral
                if usr_str[index:index+2] == numeral:
                    # Set holding_val to the found value  
                    holding_val = value
                    # Flag that a double character roman numeral was found
                    double_found = True
                    # Move on to the next character
                    break

                # Check if this current character matches this roman numeral
                elif char == numeral:
                    # Temporarely hold the resulting integer in case a two character is found
                    holding_val = value

            # Add the found value to the final result
            result += holding_val
        
        # Check to make sure it's only a roman numeral between I and MMMCMXCIX
        if result >= 4000:
            raise ValueError("Enter a valid roman numeral between I and MMMCMXCIX")

        # Set the class var result to be the deconvert result MMMCMXCIX
        self.result = result


if __name__ == "__main__":
    # Get user input with a prompt
    value = input("Please input a integer between 0 and 3999: ")

    # Create a converter with input
    converter = Roman(value)

    # Convert the input
    converter.convert()
    print("Convert is: ", converter.result)

    # Get user input with a prompt
    value = input("Please input a roman numeral between I and MMMCMXCIX: ")

    # Set the converter's value to the input
    converter.value = value

    # Deconvert the input
    converter.deconvert()
    print("Deconvert is: ", converter.result)
