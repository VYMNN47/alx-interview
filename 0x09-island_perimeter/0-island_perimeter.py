#!/usr/bin/python3
"""Module for island_perimeter"""


def island_perimeter(grid):
    """
    Finds the perimeter of the island described in grid

    Attributes:
        grid: given grid

    Returns:
        perimeter of grid
    """

    visit = set()

    def dfs(i, j):
        """
        Depth-first search function that traverse the grid and identifies
        perimeter of each cell

        Attributes:
            i: grid rows
            j: grind columns

        Returns:
            returns 1 if a cell perimeter is found other wise 0
        """

        if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 \
                or grid[i][j] == 0:
            return 1

        if (i, j) in visit:
            return 0

        visit.add((i, j))

        perim = dfs(i, j + 1)
        perim += dfs(i + 1, j)
        perim += dfs(i, j - 1)
        perim += dfs(i - 1, j)

        return perim

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                return dfs(i, j)
    return 0
