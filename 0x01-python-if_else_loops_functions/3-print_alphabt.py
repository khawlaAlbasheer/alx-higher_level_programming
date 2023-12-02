#!/usr/bin/python3
for i in range(97, 123):
    c = chr(i)
    if c == 'e' or c == 'q':
        pass
    else:
        print('{}'.format(c), end="")
