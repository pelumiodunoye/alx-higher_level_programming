#!/usr/bin/python3

def no_c(my_string):
    iyanu = ""
    for a in range(len(my_string)):
        if my_string[a] != 'c' and my_string[a] != 'C':
            iyanu += my_string[a]
    return (iyanu)
