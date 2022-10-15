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
        self.width = super().validate(value, "width")
