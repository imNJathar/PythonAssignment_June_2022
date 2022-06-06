
"""
Write a function that will take one list as input and return three different types of list as illustrated in the output.
In object2, you can append a list containing triplet of a number but object 3 should be evaluated based on the elements
present in the object2 (Note:You have to take care of both the space and time complexities as well)
Input:
object1 = [[1,1,1],[2,2,2],[3,3,3]]

Output:
object1 = [[1,1,1],[2,2,2],[3,3,3]]
object2 = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]
object3 = [[1,1,1],[2,4,2],[3,9,3],[4,16,4]]
"""


def list_operations(lst1):
    """
    This function displays output on the basis of given list
    :param lst1: list of elements
    :return:
    """
    len_list = len(lst1)
    print(lst1)
    lst1.append([i + 1 for i in lst1[len_list - 1]])
    print(lst1)

    for i in range(0, len_list-2):
        for j in lst1:
            j[len(j)//2] = j[len(j)//2]**2
    print(lst1)


if __name__ == "__main__":
    lst = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    list_operations(lst)