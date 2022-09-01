#!/usr/bin/python3

from re import S


def only_diff_elements(set_1, set_2):
    a = set_1
    b = set_2
    newset = a.union(b)
    newset.remove ('C')
    return (newset)