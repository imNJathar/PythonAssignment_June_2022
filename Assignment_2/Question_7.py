
"""
Write a program using loops and closure to find the multipliers of 4 (4,8,12,16,....,40)?
"""


def multipliers_of_num(num1):
    """
    This function will print multipliers of number
    :param num1: integer number
    """
    if num1 > 0:
        for i in range(1, 11):
            print(num1*i, end=" ")


def multipliers_of_num_closure(num1):
    """
    This function will print multipliers of number
    :param num1: integer number
    """
    num1 = num1
    def inner_func():
        for i in range(1, 11):
            print(num1*i, end=" ")
    return inner_func


if __name__ == "__main__":
    num1 = int(input("Please enter number : "))

    multipliers_of_num(num1)
    print("\n")
    obj = multipliers_of_num_closure(num1)
    obj()
