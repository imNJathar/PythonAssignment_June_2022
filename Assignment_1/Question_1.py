

"""
Write any python program that makes use of variables, constants, operators, at least 5
keywords and print statements of different forms ?
keywords : import, def, return, if, not
"""

import math


def calculate_area_of_circle(radius):
    """
    This function will calculate area of circle
    :param radius: radius of circle
    :return: return area of circle
    """
    if not radius > 0:
        return 0
    result = math.pi * (radius * radius)
    return result


def calculate_area_of_triangle(base, height):
    """
    This function will calculate area af triangle
    :param base: base of triangle
    :param height: height of triangle
    :return: return area of triangle
    """
    if not base > 0 or not height:
        return 0
    result = (base * height) / 2
    return result


if __name__ == "__main__":
    radius = int(input("Please enter the radius of circle : "))
    area_of_circle = calculate_area_of_circle(radius)
    if not area_of_circle:
        print("Radius should not be negative")
    else:
        print(f"Area of circle of radius {radius} is {area_of_circle}")

    base = int(input("Please enter the base of triangle : "))
    height = int(input("Please enter the height of triangle : "))
    area_of_triangle = calculate_area_of_triangle(base, height)
    if not area_of_circle:
        print("Base or Height should not be negative")
    else:
        print(f"Area of triangle of base {base} and height {height} is {area_of_triangle}")
