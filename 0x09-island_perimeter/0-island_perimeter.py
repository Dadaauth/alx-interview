#!/usr/bin/python3
"""ALXSWE Island perimeter Project
"""


def island_perimeter(grid):
    """
    Computes and returns
    the perimeter of the
    island described in grid
    """
    if type(grid) != list:
        return 0

    peri = 0
    n = len(grid)

    for f, row in enumerate(grid):
        m = len(row)
        for k, cell in enumerate(row):
            if cell == 0:
                continue
            egdges = (
                f == 0 or (len(grid[f - 1]) > k and grid[f - 1][k] == 0),
                k == m - 1 or (m > k + 1 and row[k + 1] == 0),
                f == n - 1 or (len(grid[f + 1]) > k and grid[f + 1][k] == 0),
                k == 0 or row[k - 1] == 0,
            )
            peri += sum(egdges)
    return peri
