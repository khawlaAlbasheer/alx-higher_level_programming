#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
if last > 5:
    string = 'and is greater than 5'
    if number < 0:
        last = -last
elif last == 0:
    string = 'and is 0'
elif last < 6 and last != 0:
    string = 'and is less than 6 and not 0'
print(f'Last digit of {number} is {last} {string}')
