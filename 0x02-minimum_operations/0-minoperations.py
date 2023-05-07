#!/usr/bin/python3
"""
this module contains functions for minimum operations

"""


def minOperations(n):
    """
    this function finds the minimum number of operations
    taken to acieve a numbered goal
    """

    if n <= 1:
        return 0

    for x in range(2, int((n/2)+1)):
        if n % x == 0:
            return minOperations(int(n / x)) + x

    return n
