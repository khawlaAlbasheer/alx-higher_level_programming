def multiple_returns(sentence):
    length = len(sentence)
    if length == 0 or sentence is None:
        return None
    first_char = sentence[0]
    return (length, first_char)
