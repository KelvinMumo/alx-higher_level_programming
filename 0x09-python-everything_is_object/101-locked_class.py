#!/usr/bin/python3
"""
Module for a class LockedClass with no class or object attribute,
that prevents the user from dynamically creating new instance attributes,
except if the new instance attribute is called first_name

"""


class LockedClass:
    """
    Defines class LockedClass

    """
    __slots__ = ['first_name']

    def __init__(self):
        """method"""
        pass
