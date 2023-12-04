#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b == 0:
        return 1
    elif b < 0:
        while b < 0:
            result = result / a
            b += 1
        return result
    elif b > 1:
        while b > 0:
            result *= a
            b -= 1
        return result
