#!/usr/bin/python3
"""
this contains the rectangle function
"""


from tempfile import gettempprefix
from turtle import width
from models.base import Base
class Rectangle(Base):
    """contains class rectangle"""


    def __init__(self, width, height, x=0, y=0, id=None):
        """iniitializes function"""
        self.id = super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y


    @property
    def width(self):
        """retrieves the  width of the rectangle"""
        return  (self.__width)


    @width.setter
    def width(self, value):
        """sets value for width"""
        self.__width = value


    @property
    def height(self):
        """retrieves the height of the rectangle"""
        return (self.__height)


    @height.setter
    def height(self, value):
        """sets value for height"""
        self.__height = value


    @property
    def x(self):
        """retrieves the value of x"""
        return (self.__x)


    @x.setter
    def x(self, value):
        """sets value for x"""
        self.__x = value


    @property
    def y(self):
        """retrieves the value of y"""
        return (self.__y)


    @y.setter
    def y(self, value):
        """sets value for y"""
        self.__y = value
