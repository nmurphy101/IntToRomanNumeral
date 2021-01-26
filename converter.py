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

        # Numbers and their respective symbols
        num = [1, 4, 5, 9, 10, 40, 50, 90,
               100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL",
               "L", "XC", "C", "CD", "D", "CM", "M"]
        # Initilize the list index and result string
        i = 12
        roman_num = ""
        # Loop so long as integer is not zero
        while integer:
            # devide integer by the current 'numbers place'
            div = integer // num[i]
            # modulus integer by the current 'numbers place'
            integer %= num[i]
            # Loop so long as the division is not zero
            while div:
                # Add the roman numeral to the result string
                roman_num += sym[i]
                div -= 1
            # Decend the number/symbol lists
            i -= 1
        # Set the final result
        self.result = roman_num

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
