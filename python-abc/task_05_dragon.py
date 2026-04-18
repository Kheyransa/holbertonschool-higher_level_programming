#!/usr/bin/python3
"""
This module demonstrates the use of mixins with the Dragon class.
"""


class SwimMixin:
    """Mixin to provide swimming functionality."""

    def swim(self):
        """Prints a swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin to provide flying functionality."""

    def fly(self):
        """Prints a flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that inherits behaviors from SwimMixin and FlyMixin.
    """

    def roar(self):
        """Prints a roaring message."""
        print("The dragon roars!")
