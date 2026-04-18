#!/usr/bin/python3
"""
This module defines the CountedIterator class that extends an iterator
to keep track of the number of items iterated over.
"""


class CountedIterator:
    """
    An iterator that keeps track of how many items have been fetched.
    """

    def __init__(self, iterable):
        """
        Initializes the iterator and the counter.

        Args:
            iterable: The collection to iterate over.
        """
        self.__iterator = iter(iterable)
        self.__count = 0

    def get_count(self):
        """Returns the current number of items iterated."""
        return self.__count

    def __next__(self):
        """
        Increments the counter and returns the next item.
        Raises StopIteration if no items are left.
        """
        try:
            item = next(self.__iterator)
            self.__count += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """Returns the iterator object itself."""
        return self
