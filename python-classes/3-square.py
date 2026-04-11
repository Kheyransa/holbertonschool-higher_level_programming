#!/usr/bin/python3
"""
This module defines a Square class that can calculate its area.
"""


class Square:
    """
    Square class that defines a square and calculates its area.
    """

    def __init__(self, size=0):
        """
        Initializes the square with size validation.

        Args:
            size (int): The size of the square's side. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            The area of the square (size squared).
        """
        return (self.__size * self.__size)
