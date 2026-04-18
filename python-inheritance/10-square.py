#!/usr/bin/python3
"""
This module contains the Square class that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A representation of a square using Rectangle.
    """

    def __init__(self, size):
        """
        Initializes the square with size.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self.__size ** 2
