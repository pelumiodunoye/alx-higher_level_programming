#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    a = a_dictionary.keys()
    if len(a) == 0:
        return(None)
    biggest = 0
    for i in a:
        if a_dictionary[i] > biggest:
            biggest = a_dictionary[i]
            name = i
    return (name)
