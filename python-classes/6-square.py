#!/usr/bin/python3
"""
This module defines a Square class with size and position.
"""


class Square:
    """
    Square class that defines a square by its size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square.

        Args:
            size (int): The size of the square's side.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with # and uses position for spaces."""
        if self.__size == 0:
            print("")
            return

        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print("")

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
