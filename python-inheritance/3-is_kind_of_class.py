#!/usr/bin/python3
"""
This module contains the function is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of, or inherited from, a_class.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        bool: True if it matches the criteria, otherwise False.
    """
    return isinstance(obj, a_class)
