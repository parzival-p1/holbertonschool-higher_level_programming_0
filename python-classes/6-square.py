#!/usr/bin/python3
""" a class Square that defines a square by: (based on 5-square.py) """


class Square:
    """ Defines a Square """

    def __init__(self, size=0, position=(0, 0)):
        """ Create a square.
        Args:
            size: size of the square.
        Raises:
            TypeError: If size is not integer.
            ValueError: If size is lower than zero.
        """
        self.size = size
        self.position = position

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

        @property
        def position(self):
            """ position: position of the square. Function Getter"""
        return (.__self.position)

        @size.setter
        def position(self, value)
        """ Position: Position of the square. Function Setter.
            Raises:
                TypeError: Pos must be a tuple of 2 positive ints
           """
        if type(value) is not tuple or len(valu) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not or value[1] < 0:
            raise TypeError("position must be a tuplee of 2 positive integers")
        else:
            self.__position = value

        def area(self):
            """ Get the area of a Square.
            Returns: Area of the square instance.
            """
            return (self.__ ** 2)

        def my_print(self):
            """ Prints the squaree """
            if self.__size == 0:
                print()
                return
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print("".join([" " for k in range(self.__position[0])]), end="")
                print("".join(["#" for l in range(self.__size)]))
