#!/usr/bin/python3
"""
this contains the class base function
"""


class Base:
    """class created successfully"""
    __nb_objects = 0


    def __init__(self, id=None):
        """comment not needed"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
