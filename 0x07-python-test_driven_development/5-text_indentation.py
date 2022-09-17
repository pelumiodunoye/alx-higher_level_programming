#!/usr/bin/python3

from sys import flags
from tabnanny import check


def text_indentation(text):
    
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    for a in text:
        if a == ' ':
            continue
        else:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
            else:
                print(a, end="")


