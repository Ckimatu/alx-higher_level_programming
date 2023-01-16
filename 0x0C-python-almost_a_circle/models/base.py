#!/usr/bin/python3

"""this module contains the class base"""


class Base:
    """ the “base” of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        self.id = id
        if self.id is not None:
            self.id = int(self.id)
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
