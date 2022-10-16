#!/usr/bin/python3
"""
this contains the square function
"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """contains class square that inheerits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes function"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns [Square] (<id>) <x>/<y> - <size>"""
        return ("[Square] ({}) {}/{} - {}" .format(
            self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """retrieves the value of size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """sets value for width"""
        self.height = super().validate(value, "width")
        self.width = super().validate(value, "width")


    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        try:
            self.id = args[0]
            self.size = super().validate(args[1], "width")
            self.x = super().validate(args[2], "x")
            self.y = super().validate(args[3], "y")
        except Exception:
            pass
        if not args:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = super().validate(kwargs["size"], "width")
            if "x" in kwargs:
                self.x = super().validate(kwargs["x"], "x")
            if "y" in kwargs:
                self.y = super().validate(kwargs["y"], "y")
