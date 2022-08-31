#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new = my_list.copy()
    for c in range(len(new)):
        if new[c] == search:
            new[c] = replace
    return (new)  