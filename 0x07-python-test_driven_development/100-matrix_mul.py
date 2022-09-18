#!/usr/bin/python3

"""
Contains the matrix_mul function
"""

def matrix_mul(m_a, m_b):
    
    """Multiply two matrices(lists of lists of integers/floats)"""
     
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
    content = len(m_a)
    if content == 0:
        raise ValueError("m_a can't be empty")
    for j in i:
        if type(j) is not int or type(j) is not float:
            raise TypeError("m_a should contain only integers or floats")
    if content != len(m_a):
        raise TypeError("each row of m_a must be of the same size")
    
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")
    content2 = len(m_b)
    if content2 == 0:
        raise ValueError("m_b can't be empty")
    for j in i:
        if type(j) is not int or type(j) is not float:
            raise TypeError("m_b should contain only integers or float")
    if content2 != len(m_b):
        raise TypeError("each row of m_b must be of the same size")
    if content != content2:
        raise ValueError("m_a and m_b can't be multiplied")
    
    matrix = []
    for i in range(content):
        new_matrix = []
        for j in range(content2):
            n = 0
            for k in range(content2):
                n += m_a[i][k] * m_b[k][j]
            new_matrix.append(n)
        matrix.append(new_matrix)
    return matrix