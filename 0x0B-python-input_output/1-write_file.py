#!/usr/bin/python3
"""
contains the write_file function
"""


def write_file(filename="", text=""):
    """writes string to a text file, returns the no. of char written"""
    with open(filename, 'w+', encoding="UTF-8") as f:
        count = f.write(text)
    return (count)
