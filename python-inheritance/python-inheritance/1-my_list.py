#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.
"""


class MyList(list):
    """
    A subclass of list that includes a method to print the list sorted.
    """

    def print_sorted(self):
        """
        Prints the list elements in ascending order.
        Assumes all elements are of type int.
        """
        print(sorted(self))
