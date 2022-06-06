
"""
Write a function that accepts a sequence of whitespace separated words as input and prints the words after removing
all duplicate words and sorting them alphanumerically? (Both with and without second list)
"""


def remove_duplicate_sort_without(string_data):
    """
    This function remove duplicate words and arrange them in sorted order
    :param string_data: input string or sentence
    :return: returns sorted list
    """
    lst1 = string_data.split(" ")
    lst1.sort()
    for i in lst1:
        if lst1.count(i) >= 2:
            lst1.pop(lst1.index(i))
    return lst1


def remove_duplicate_sort(string_data):
    """
    This function remove duplicate words and arrange them in sorted order
    :param string_data: input string or sentence
    :return: returns sorted list
    """
    return sorted(set(string_data.split(" ")))


if __name__ == "__main__":
    string = input("Please enter string : ")

    sorted_list = remove_duplicate_sort(string)
    print(f"Sorted list for string '{string}' is {sorted_list}")

    sorted_list1 = remove_duplicate_sort_without(string)
    print(f"Sorted list for string '{string}' is {sorted_list1}")
