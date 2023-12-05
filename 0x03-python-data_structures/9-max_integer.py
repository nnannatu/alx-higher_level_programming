#!/usr/bin/python3
# Function that finds the biggest integer of a list

def max_integer(my_list=[]):
    if my_list:
        for i in my_list:
            if my_list[i] < my_list[i + 1]:
                return my_list[i + 1]
            else:
                return my_list[i]
    else:
        return None
