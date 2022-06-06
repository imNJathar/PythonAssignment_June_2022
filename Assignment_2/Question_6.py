
"""
Write a program to find the maximum of 2 numbers using normal function and then using ternary operator and
then illustrate the same using lambda function ?
"""


def max_of_num(num1, num2):
    """
    This function will find maximum number from two numbers
    :param num1: first num
    :param num2: second num
    :return: return max number
    """
    if num1 > num2:
        return num1
    return num2


def max_of_num_ter(num1, num2):
    """
    This function will find maximum number from two numbers
    :param num1: first num
    :param num2: second num
    :return: return max number
    """
    return num1 if num1 > num2 else num2


def max_of_num_lambda(num1, num2):
    """
    This function will find maximum number from two numbers
    :param num1: first num
    :param num2: second num
    :return: return max number
    """
    max = lambda num1, num2: num1 if num1 > num2 else num2
    return max(num1, num2)


if __name__ == "__main__":
    num1 = int(input("Please enter first number : "))
    num2 = int(input("Please enter second number : "))

    max_num = max_of_num(num1, num2)
    print(f"Maximum number from {num1} and {num2} is {max_num}")

    max_num = max_of_num_ter(num1, num2)
    print(f"Maximum number from {num1} and {num2} is {max_num}")

    max_num = max_of_num_lambda(num1, num2)
    print(f"Maximum number from {num1} and {num2} is {max_num}")