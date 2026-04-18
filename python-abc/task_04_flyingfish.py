#!/usr/bin/python3
"""
This module demonstrates multiple inheritance with Fish, Bird, and FlyingFish.
"""


class Fish:
    """Class representing a Fish."""

    def swim(self):
        """Prints swimming message."""
        print("The fish is swimming")

    def habitat(self):
        """Prints fish habitat."""
        print("The fish lives in water")


class Bird:
    """Class representing a Bird."""

    def fly(self):
        """Prints flying message."""
        print("The bird is flying")

    def habitat(self):
        """Prints bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Class representing a FlyingFish that inherits from Fish and Bird.
    """

    def fly(self):
        """Overrides Bird fly method."""
        print("The flying fish is soaring!")

    def swim(self):
        """Overrides Fish swim method."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Overrides both Fish and Bird habitat methods."""
        print("The flying fish lives both in water and the sky!")
