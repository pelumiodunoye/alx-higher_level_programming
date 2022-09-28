#!/usr/bin/python3
"""
contains the write_file function
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns the number of characters written"""
    with open(filename, 'r', encoding="utf-8") as f:
        i = 0
        for line in f:
            i += 1
        return i 
