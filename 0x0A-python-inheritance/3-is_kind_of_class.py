#!/usr/bin/python3
"""
Module is_kind_of_class - Contains 3-is_kind_of_class function

"""


def is_kind_of_class(obj, a_class):
    """
    Checks if if the object is an instance of a class
    that inherited from the specified class

    Args:
        obj (any): object to check
        a_class (type): class to match the object to

    Return:
        True if the object is an instance of, or if the object is an instance of a class
        that inherited from, the specified class;
        Otherwise, return False.
    """
    if isinstance(obj, a_class):
        return True
    return False
