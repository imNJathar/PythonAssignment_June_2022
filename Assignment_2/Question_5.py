
"""
Write a function that takes the path of a directory and prints out the paths files within that directory as well as any
files present in the nested directories. (This function is similar to os.walk. Please don't use os.walk in your answer.
We are interested in your ability to work with nested structures)
"""

import os


def print_all_nested_file_dir(path):
    """
    This Function will print all nested file and directories
    :param path: valid path in string form
    """

    if not os.path.isdir(path):
        return
    all_dir = os.listdir(path)
    print(path, all_dir)
    for i in all_dir:
        print_all_nested_file_dir(f"{path}\\{i}")


if __name__ == "__main__":
    path = "D:\\Work\\project\\Company\\Artifacts"
    print_all_nested_file_dir(path)
