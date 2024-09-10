#!/usr/bin/python3
"""Module for rotate_2d_matrix"""


def rotate_2d_matrix(matrix):
    """Rotate it 90 degrees clockwise"""

    for i in range(0, len(matrix)):
        for j in range(i, len(matrix)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for row in matrix:
        row.reverse()
