#!/usr/bin/python3

"""
this module contains functions for computing
a pascal triangle.

"""


def pascal_triangle(n):
    """ this function computes a pascal triangle
    the function returns a list of lists containing the
    values of the pascal triangle"""

    result = []
    if n <= 0:
        return result
    for i in range(1, n+1):
        c = 1
        myList = []
        for j in range(1, i+1):
            myList.append(c)
            c = c * (i - j) // j
        result.append(myList)
    return result
