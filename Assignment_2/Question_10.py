
"""
Write a program to find the sum of the digits of the number recursively upto n iterations?
"""


def find_sum_of_digits(num1):
    """
    This function will return sum of digits
    :param num1: input digit type integer
    :return: returns sum of digits
    """
    if num1 == 0:
        return 0
    num2 = num1 % 10
    return num2 + find_sum_of_digits(int(num1 / 10))


if __name__ == "__main__":
    num1 = int(input("Please enter number : "))
    sum1 = find_sum_of_digits(num1)
    print(f"Sum of digits for number {num1} is {sum1}")
