#!/usr/bin/python3
"""
This module defines a Rectangle class that counts its instances.
"""


class Rectangle:
    """
    Rectangle class that defines a rectangle and tracks the number of instances.

    Attributes:
        number_of_instances (int): The number of active Rectangle instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle using #."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = ""
        for i in range(self.__height):
            rect_str += ("#" * self.__width)
            if i != self.__height - 1:
                rect_str += "\n"
        return rect_str

    def __repr__(self):
        """Returns a string representation to recreate the instance."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Decrements the instance count and prints a message."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
