#!/usr/bin/python3

def uppercase(str):
    for i in str(97, 113):
        if ord(i) >= 97 and ord(i) <= 113:
            i = ord(i) - 32
        else:
            i = ord(i)
        print("{:c}".format(i), end=' ')
    print()    
