#!/usr/bin/python3
""" a class Square that defines a square by: (based on 4-square.py) """


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

    @property
    def size(self):
        """ size: Size of the square. Function Getter """
        return (self.__size)

    @size.setter
    def size(self, value):
        """size: Size of the square. Function Setter.
        Raises:
            TypeError: If size is not integer.
            ValueError: If size is lower than zero.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ my_print: Prints the square size """
        if self.__size == 0:
            print()
            return ()
        for col in range(self.__size):
            for row in range(self.size):
                print("#", end="")
            print()
