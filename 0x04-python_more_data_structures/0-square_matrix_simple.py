#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        new[len(new):] = [[elem ** 2 for elem in i]]
    return new
