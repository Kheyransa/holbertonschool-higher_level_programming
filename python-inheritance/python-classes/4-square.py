#!/usr/bin/python3
"""
This module defines a Square class with getter and setter for size.
"""


class Square:
    """
    Square class that defines a square by its size.
    """

    def __init__(self, size=0):
        """
        Initializes the square.

        Args:
            size (int): The size of the square's side. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size with validation.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            The area of the square.
        """
        return (self.__size * self.__size)
