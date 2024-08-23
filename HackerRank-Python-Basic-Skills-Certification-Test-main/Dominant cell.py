#!/bin/python3

import os
import sys

#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def numCells(grid):
    n = len(grid)
    m = len(grid[0])
    
    # Directions for the 8 neighbors: (row offset, column offset)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def is_dominant(row, col):
        cell_value = grid[row][col]
        for d in directions:
            new_row, new_col = row + d[0], col + d[1]
            if 0 <= new_row < n and 0 <= new_col < m:
                if grid[new_row][new_col] >= cell_value:
                    return False
        return True
    
    count = 0
    for i in range(n):
        for j in range(m):
            if is_dominant(i, j):
                count += 1
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
