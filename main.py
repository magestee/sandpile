import numpy as np

def iterate(grid):
    changed = False
    for ii, arr in enumerate(grid):
        for jj, val in enumerate(arr):
            if val > 3:
                grid[ii, jj] -= 4
                if ii > 0:
                    grid[ii - 1, jj] += 1
                if ii < len(grid)-1:
                    grid[ii + 1, jj] += 1
                if jj > 0:
                    grid[ii, jj - 1] += 1
                if jj < len(grid)-1:
                    grid[ii, jj + 1] += 1
                changed = True
    return grid, changed


def simulate(grid):
    while True:
        grid, changed = iterate(grid)
        if not changed:
            return grid


start_grid = np.zeros((10, 10))
start_grid[4:5, 4:5] = 64
final_grid = simulate(start_grid.copy())
print(start_grid)
print(final_grid)
