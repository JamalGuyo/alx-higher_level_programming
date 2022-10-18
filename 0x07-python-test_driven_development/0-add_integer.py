#!/usr/bin/python3


def add_integer(a, b=98):
    """add integer function
    raise:
        TypeError - a and b must be integers
                    message = 'a must be an integer' or b
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    if type(a) in [float]:
        a = int(a)
    if type(b) in [float]:
        b = int(b)
    return a + b
