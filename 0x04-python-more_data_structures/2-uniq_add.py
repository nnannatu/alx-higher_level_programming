#!/usr/bin/python3

def uniq_add(my_list=[]):
    '''
    Function that adds all unique integers in
    a list (only once for each integer)
    '''
    new_list = []
    add_num = 0
    for item in my_list:
        if item not in new_list:
            add_num += item
            new_list.append(item)
    return add_num
