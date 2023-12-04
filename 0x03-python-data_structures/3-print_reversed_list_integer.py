#!/usr/bin/python3
# Function that prints all intergers of a list in reverse order

def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list = my_list[::-1]
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i]))
