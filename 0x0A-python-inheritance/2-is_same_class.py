#!/usr/bin/python3

"""Module 2-is_same_class - Contains is_same_class_function"""


def is_same_class(obj, a_class):
    """
    Checks if the object is an instance of the specified class

    Args:
        obj (any): The object to check
        a_class (type): the class to match the type of obj to

    Return:
       True if the object is exactly an instance of the specified class 
       Otherwise, return False
    """
    if type(obj) is  a_class:
        return True
    return False
