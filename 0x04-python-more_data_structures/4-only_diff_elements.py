#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    a = set_1
    b = set_2
    newset = a.union(b)
    newset.remove ('C')
    return (newset)
