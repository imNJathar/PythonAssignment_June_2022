
"""
Write a program to exchange the values of two numbers without using a temporary variable.
"""


def swap_values(val1, val2):
    """
    This function will swap values without using extra variable
    :param val1: any value type int
    :param val2: any value type int
    :return: returns swapped values type int
    """

    '''
    # This is another way to swap values 
    val1 ^= val2
    val2 ^= val1
    val1 ^= val2
    return val1, val2
    '''
    val1, val2 = val2, val1
    return val1, val2


if __name__ == "__main__":
    first_num = int(input("Please enter first value : "))
    second_num = int(input("Please enter second value : "))

    print(f"Values before swapping {first_num} and {second_num}")
    first_num, second_num = swap_values(first_num, second_num)

    print(f"Values after swapping {first_num} and {second_num}")
