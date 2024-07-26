#!/usr/bin/python3
"""returns list of lists of integers representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """Pascal's Triange"""
    results = [[1]]
    if not n:
        return []

    for i in range(n - 1):
        temp = [0] + results[-1] + [0]
        row = []
        for j in range(len(results[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        results.append(row)

    return results
