#!/usr/bin/python3
""" A module called square.py file"""


class Square:
    """ A class defining square"""

    def __init__(self, size=0):
        """initialise Square class
        Args:
            size: private instance must be an integer
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than 0
        """
        if isinstance(size, int):
            if size > 0:
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """area public method
        Args:
            self: current object
        Returns:
            current square area
        """
        return self.__size ** 2
