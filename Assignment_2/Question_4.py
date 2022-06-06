
"""
Given an array of ints length n, return an array with the elements "rotated left" so {1, 2, 3} yields each
iteration until {2, 3, 1} comes. Eg:
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]
"""

import array as arr


def left_rotate(arr_ele):
    """
    This function rotate array in left
    :param arr_ele: input array of integer
    :return: ret lef rotate arr
    """
    cnt = 0
    len_arr = len(arr_ele)-1
    while cnt <= len_arr:
        temp = arr_ele[cnt]
        arr_ele[cnt] = arr_ele[len_arr]
        arr_ele[len_arr] = temp
        cnt += 1
        len_arr -= 1
    return arr_ele


if __name__ == "__main__":
    arr_ele = int(input("enter how many element array? "))
    if arr_ele >= 3:
        print("Enter elements : ")
        lst1 = []
        for i in range(0, arr_ele):
            ele = int(input())
            lst1.append(ele)
        arr_ele = arr.array('i', lst1)
        print(f"Array before rotating {arr_ele}")
        rotate_list = left_rotate(arr_ele)
        print(f"Array after rotating {rotate_list}")
    else:
        print("Number is not greater than 3")
