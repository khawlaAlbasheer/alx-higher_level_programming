#!/usr/bin/python3
for i in range(9):
    for j in range(i+1, 10):
        print('{}{}'.format(i, j), end="")
        if i == 8 and j == 9:
            continue
        print(', ', end="")
print('\n', end="")
