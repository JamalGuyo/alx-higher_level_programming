#!/usr/bin/python3
"""
class Square defines square.instantiate with size = 0
Args:
    size - must be an integer
    ,otherwise raise TypeError with message 'size must be an integer'
    if size < 0 raise ValueError with message 'size must be >= 0
Returns:
    None
"""


class Square:
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')
