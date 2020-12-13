"""
Determine the number of trees you would encounter if, for each of the following slopes,
you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?
"""

import numpy as np
from part1 import extend_map

if __name__ == "__main__":

    with open("input.txt", "r") as f:
        data = f.read()
    contents = [list(row) for row in data.split("\n")]
    data_array = np.array(contents)

    m1 = {"right": 1, "down": 1}
    m2 = {"right": 3, "down": 1}
    m3 = {"right": 5, "down": 1}
    m4 = {"right": 7, "down": 1}
    m5 = {"right": 1, "down": 2}

    subtotals = []
    for movements in [m1, m2, m3, m4, m5]:

        y = 0
        x = 0
        trees = 0

        custom_map = extend_map(data_array, movements["right"])
        while True:
            try:
                current_position = custom_map[y, x]
                y += movements["down"]
                x += movements["right"]
                if current_position == "#":
                    trees += 1
            except IndexError:
                print(
                    f"Based on {movements} trajectory, {trees} trees will be encountered"
                )
                subtotals.append(trees)
                break

    print(f"\nSolution: product is {np.prod(subtotals)}")
