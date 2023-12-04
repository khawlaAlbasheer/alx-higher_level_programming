#!/usr/bin/python3
def uppercase(str):
    for c in str:
        up = ord(c)
        if up >= 97 and up <= 122:
            up -= 32
        print('{}'.format(chr(up)), end="")
    print()
