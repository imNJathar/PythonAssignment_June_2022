
"""
Write a program to read two numbers and print their quotient and remainder.
"""


def print_quotient_remainder(val1, val2):
    """
    This function will print quotient and remainder of given values
    :param val1: any value type int
    :param val2: any value type int
    """
    print(f"Remainder and Quotient for number {val1} and {val2} is {val1 // val2} and {val1 % val2}")


if __name__ == "__main__":
    first_num = int(input("Please enter first value : "))
    second_num = int(input("Please enter second value : "))

    print_quotient_remainder(first_num, second_num)

