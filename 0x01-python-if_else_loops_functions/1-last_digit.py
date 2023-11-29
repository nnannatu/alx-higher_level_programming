#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
'''Rem: while reviewing, that you cannot manipulate int, \
        that's why I've to convert to str first to do my \
        incantations before converting back to int.
'''
last_digit = int(str(number)[-1])
if number < 0:
    last_digit = -last_digit
if last_digit > 5:
    print(f'Last digit of {number} is {last_digit} and is greater than 5')
elif last_digit == 0:
    print(f'Last digit of {number} is {last_digit} and is 0')
else:
    print(f'Last digit of {number} is {last_digit} and is less than 6 and not 0')
