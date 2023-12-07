#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    '''
    Function that deletes keys with
    a specific value in a dictionary
    '''
    list_keys = list(a_dictionary.keys())

    for val in list_keys:
        if value == a_dictionary.get(val):
            del a_dictionary[val]
    return (a_dictionary)
