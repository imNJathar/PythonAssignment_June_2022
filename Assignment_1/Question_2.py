
"""
Write a program to find modulus of a complex number 8+6j.
|X| = sqrt(a*2 + b*2)
"""

import math


def find_modulus_of_complex_number(complex_number:complex):
    """
    This Function calculates modules of complex number
    :param complex_number: input number type is complex
    :return: modulus: Returns modulus of complex number in float otherwise returns 0
    """

    modulus = 0
    # checking number is complex number or not
    if type(complex_number) == complex:
        a = complex_number.real
        b = complex_number.imag
        return math.sqrt(a**2 + b**2)

    return modulus


if __name__ == "__main__":
    complex_number = complex(input("Please enter complex number : "))
    result = find_modulus_of_complex_number(complex_number)
    print(f"Modulus of complex number {complex_number} is {result}")
