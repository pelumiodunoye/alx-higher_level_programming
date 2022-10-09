#!/usr/bin/python3
"""
this contains the rectangle function
"""


from models.base import Base


class Rectangle(Base):
    """contains class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """iniitializes function"""
        super().__init__(id)
        self.__width = super().validate(width, "width")
        self.__height = super().validate(height, "height")
        self.__x = super().validate(x, "x")
        self.__y = super().validate(y, "y")

    @property
    def width(self):
        """retrieves the  width of the rectangle"""
        return  (self.__width)

    @width.setter
    def width(self, value):
        """sets value for width"""
        self.__width = super().validate(value, "width")

    @property
    def height(self):
        """retrieves the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets value for height"""
        self.__height = super().validate(value, "height")

    @property
    def x(self):
        """retrieves the value of x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """sets value for x"""
        self.__x = super().validate(value, "x")

    @property
    def y(self):
        """retrieves the value of y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """sets value for y"""
        self.__y = super().validate(value, "y")

    def area(self):
        """returns the  area value of the Rectangle instance"""
        return (self.__width * self.__height)

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        row = self.__height
        column = self.__width
        for i in range(self.__y):
            print()
        for i in range(row):
            for s in range(self.__x):
                print(" ", end="")
            for j in range(column):
                print("#", end="")
            print()

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    def update(self, *args):
        """assigns an argument to each attribute"""
        try:
            self.id = args[0]
            self.__width = super().validate(args[1], "width")
            self.__height = super().validate(args[2], "height")
            self.__x = super().validate(args[3], "x")
            self.__y = super().validate(args[4], "y")
        except Exception:
            pass
