#!/usr/bin/python3
"""
Module 4-inherits_from - Contains inherits_from function

"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class,
    that inherited from a specified class

    Args:
        obj (any): the object to check
        a_class (type): the class to match the type of obj to

    Return:
        True if the object is an instance of a class
        that inherited (directly or indirectly) from the specified class;
        Otherwise return False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
