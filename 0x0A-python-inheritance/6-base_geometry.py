#!/usr/bin/python3
"""Inheritance module"""


class BaseGeometry:
    """Base geometry class"""
    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")
