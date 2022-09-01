#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    newdict = a_dictionary.copy()
    my_dict = a_dictionary.keys()
    for i in my_dict:
        newdict[i] = 2 * newdict.get(i)
    return(newdict)
