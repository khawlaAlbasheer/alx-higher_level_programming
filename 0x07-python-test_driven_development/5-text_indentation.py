#!/usr/bin/python3
""""""


def text_indentation(text):
    """"""

    if type(text) is not str:
        raise TypeError('text must be a string')
    special_char = ['.', '?', ':']
    index = 0
    while index in range(len(text)):
        if text[index] in special_char:
            if text[index + 1] == ' ':
                print(text[index])
                print()
                index += 2
        else:
            print(text[index], end='')
            index += 1
