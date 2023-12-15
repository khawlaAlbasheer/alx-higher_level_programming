#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return None
    elif len(sentence) == 0:
        first_char = ''
        return (len(sentence), first_char)
    first_char = sentence[0]
    length = len(sentence)
    return (length, first_char)
