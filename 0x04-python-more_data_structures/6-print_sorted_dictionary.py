#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    '''
    Function that prints a dictionary by ordered keys.
    '''
    sort_list = dict(sorted(a_dictionary.items()))
    for key, value in sort_list.items():
        print("{}: {}".format(key, value))
