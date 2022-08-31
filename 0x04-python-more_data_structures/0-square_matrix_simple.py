#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new = []
    for i in range(len(matrix)):
        n_ew = list(map(lambda x: x*x, matrix[i]))
        new.append(n_ew)
    return (new)
