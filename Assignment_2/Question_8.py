
"""
Write a program to illustrate the use of default, keyword, optional and variable length args (*args and **kwargs)?
"""


def keyword_arg(name, dob, city, country="india"):
    """
    This function will display info of people
    :param name: name in string
    :param dob: dob in string
    :param city: city in string
    :param country: country in string default is india and its optional
    """

    print(f"Name is {name}")
    print(f"DOB is {dob}")
    print(f"City is {city}")
    print(f"country is {country}")


def default_n_optional_arg(num=5):
    """
    This function will get factorial of number
    :return: fact: factorial of number if given
    """
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact


def addition_of_multiple_numbers(*args):
    """
    This function will add all numbers
    :param args: Variable argument type list
    :return: sum_of_num sum of all numbers
    """
    sum_of_num = 0
    for i in args:
        sum_of_num += i
    return sum_of_num


def print_data_emp(**kwargs):
    """
    This function will pint
    :param kwargs:
    """
    for key, value in kwargs.items():
        print("{} is {}".format(key, value))


if __name__ == "__main__":
    sum1 = addition_of_multiple_numbers(10, 20, 30, 40)
    print(f"Sum of numbers is {sum1}")

    sum1 = addition_of_multiple_numbers(100, 5, 300, 40, 50, 70)
    print(f"Sum of numbers is {sum1}")

    print_data_emp(Name="Amit Sharma", Age=30, emp_id=80224, Phone_number=9854676745, DOB="16/11/1992", Blood_Group="A+")

    num1 = int(input("Please enter number : "))
    ret = default_n_optional_arg(num1)
    print(f"Factorial of number is {ret}")
    ret = default_n_optional_arg()
    print(f"Factorial of number is {ret}")

    keyword_arg("Jos", "16/11/1998", "LA", "US")
    keyword_arg("vishal", "21/07/1996", "Pune")
