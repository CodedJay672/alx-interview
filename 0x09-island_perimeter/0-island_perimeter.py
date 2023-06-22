#!/usr/bin/python3
"""
  island perimeter module

"""


def island_perimeter(grid):
    """ function which calculates the perimeter of the island
    This function uses the following logic:
        we iterate over the elements in the grid
            if an element is 1, representing land, we add 4 to
                the perimeter.
            if the element to the right is also 1,
                we subtract one
    """
    if len(grid) > 100 or len(grid[0]) > 100:
        return

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
    return perimeter
