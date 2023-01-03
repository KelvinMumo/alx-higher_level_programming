#!/usr/bin/python3

"""Module 4-square: class Square

"""


class Square:
    """
    defines class Square

    """

    def __init__(self, size=0):
        """
        Initializes a square

        Args:
            size: size of square
        """
        self.size = size

    @property
    def size(self):
        """Current size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set size

        Args:
            value: sets size to value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the area of the square

        """
        return (self.__size)**2
