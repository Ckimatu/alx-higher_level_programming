#!/usr/bin/python3

"""module with no class or object attribute"""


class LockedClass:
    """contains no class or object attribute and 
    prevents the user from dynamically creating new instance attrbutes,
    except  if the new instance attribute is called first_name."""

    __slots__ = ["first_name"]
