#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    a = set_1
    b = set_2
    d = {*()}
    d.update(a)
    d.update(b)
    for a in set_1:
        for b in set_2:
            if a == b:
                d.remove(b)
    return (d)
