#!/usr/bin/python3
'''Program that Print numbers'''
for number in range(0, 100):
    if number == 99:
        print('{}'.format(number))
    else:
        print("{:02}".format(number), end=", ")
