#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    newlist = my_list.copy()
    if idx < 0:
        return (newlist)
    if idx > len(newlist) - 1:
        return (newlist)
    newlist[idx] = element
    return (newlist)
