#!/usr/bin/python3
"""  a class Square that defines a square by: (based on 2-square.py) """


class Square:
    """ Defines a Square """

    def __init__(self, size=0):
        """ Create a square.
        Args:
            size: size of the square.
        Raises:
            TypeError: If size is not integer.
            ValueError: If size is lower than zero.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Get the area of a Square.
        Returns: Area of the square instance.
        """
        return (self.__size ** 2)
