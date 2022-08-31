#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new = []
    for i in range(len(matrix)):
        new2 = list(map(lambda x: x*x, matrix[i]))
        new.append(new2)
    return (new)
