"""
Due to the local geology, trees in this area only grow on exact integer coordinates in a grid.
You make a map (your puzzle input) of the open squares (.) and trees (#) you can see.
The same pattern repeats to the right as many times as necessary.

From your starting position at the top-left, check the position that is right 3 and down 1.
Then, check the position that is right 3 and down 1 from there, and so on
until you go past the bottom of the map.

Starting at the top-left corner of your map and following a slope of right 3 and down 1,
how many trees would you encounter?

"""

import numpy as np
import math

MOVEMENTS = {"right": 1, "down": 1}


def extend_map(map, right: int):
    """
    Extend the map horizontally (i.e. repeat the terrain) by a minimum number of times needed
    such that the toboggan rider does not go out of bounds (i.e. IndexError) before reaching
    the bottom of the slope.

    This essentially depends on the horizontal part of the rider's trajectory / path.
    For example, if the rider tends to move right by a lot each time,
    then the map needs to be larger to provide more room.
    """
    map = map.copy()
    map_extend_interval = len(map[0]) // right
    extension = math.ceil(map.shape[0] / map_extend_interval)
    return np.hstack([map] * extension)


if __name__ == "__main__":

    with open("input.txt", "r") as f:
        data = f.read()
    contents = [list(row) for row in data.split("\n")]
    data_array = np.array(contents)
    data_array = extend_map(data_array, MOVEMENTS["right"])

    y = 0
    x = 0
    trees = 0
    while True:
        try:
            current_position = data_array[y, x]
            y += MOVEMENTS["down"]
            x += MOVEMENTS["right"]
            if current_position == "#":
                trees += 1
        except IndexError:
            break

    print(
        f"Solution: Based on {MOVEMENTS} trajectory, {trees} trees will be encountered"
    )
