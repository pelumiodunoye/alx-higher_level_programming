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
        super()

        return ("[Square] () {}/{} - {}".format(
                super().__x, Rectangle.__y, Rectangle.__width))
