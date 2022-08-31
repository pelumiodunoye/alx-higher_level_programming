#!/usr/bin/python3

def uniq_add(my_list=[]):
    new = []
    count = 0
    for c in range(len(my_list)):
        for i in range(len(new)):
            if new[i] == my_list[c]:
                count = 1
        if count != 1:
            new.append(my_list[c])
        count = 0
    return (sum(new))
