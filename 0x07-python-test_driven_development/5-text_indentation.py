#!/usr/bin/python3

"""prints a text"""


def text_indentation(text):
    """prints a text with 2 new lines after: ., ? and :
    text must be a string, otherwise raise a TypeError
    no space at the beginning or at the end of each printed line"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
