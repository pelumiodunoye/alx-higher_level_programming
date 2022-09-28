#!/usr/bin/python3
"""
contains the write_file function
"""


def write_file(filename="", text=""):
    """writes a string to a text file and returns the number of characters written"""
    with open(filename, 'w+', encoding="UTF-8") as f:
        count = f.write(text)
    return (count)
