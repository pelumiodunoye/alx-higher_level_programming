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
        return (self.id)

    def validate(self, value, name):
        """validates the name of the name of base input"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            if name is "width" or name is "height":
                raise ValueError("{} must be > 0".format(name))
            elif value < 0:
                raise ValueError("{} must be >= 0".format(name))
        return (value)
