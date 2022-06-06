
"""
Write a function to reverse words of the sentence?(Check the output carefully)
Input:
“I love programming.”
Output:
“.programming love I”
"""


def reverse_sentence(sentence):
    """
    This function will reverse the input string and return reversed whole string
    :param sentence: input string or sentence
    :return: returns reverse string
    """
    return ' '.join(sentence.split(" ")[::-1])


if __name__ == "__main__":
    string = input("Please enter string : ")

    rev_string = reverse_sentence(string)
    print(f"The reversed string of '{string}' is '{rev_string}'")
