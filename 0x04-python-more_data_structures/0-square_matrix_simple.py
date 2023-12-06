#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    '''
    Function that computes the square
    value of all integers of a matrix
    '''
    new_matrix = []
    for row in matrix:
        squared_row = []
        for col in row:
            square = col ** 2
            squared_row.append(square)
        new_matrix.append(squared_row)
    return new_matrix
