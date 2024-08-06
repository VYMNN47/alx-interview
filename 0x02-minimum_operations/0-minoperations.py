#!/usr/bin/python3
"""Module for minOperations"""


def minOperations(n):
    """
    a method that calculates the fewest number of operations needed to result
    in exactly n H characters in the file.
    """
    if n < 2:
        return 0
    counter = 0
    i = 2
    while n > 1:
        while n % i == 0:
            counter += i
            n /= i
        i += 1
    return counter
