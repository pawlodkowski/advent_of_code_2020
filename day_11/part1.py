"""
Part 1 of https://adventofcode.com/2020/day/11
"""

import numpy as np


def read_data(filename: str) -> np.array:
    with open(filename, "r") as f:
        data = f.read()
    contents = [list(row) for row in data.split("\n")]
    data_array = np.array(contents)
    return data_array


def get_adjacents(seat: list, grid: np.array) -> np.array:

    """
    Given a list of 2 numbers corresponding to the coordinates
    of a given seat in a 2-dimensional grid (e.g. [0,0]),
    return an array that contains all the seat values
    (e.g. 'L', '.', or '#') that are adjacent to the given seat.

    For most cases, this returns 8 numbers: (the eight positions
    immediately up, down, left, right, or diagonal from the seat).

    However, it gets tricky for seats that are along the edge of the grid;
    due to the nature of NumPy slicing, seats in the corners and along the
    edges need to be processed on a (somewhat clunky) case-by-case basis.

    Prior to returning the array of adjacent seats, the given seat itself
    is removed from the array.
    """

    # Upper Left-Hand Corner (special case)
    if seat[0] == 0 and seat[1] == 0:
        adjacents = grid[seat[0] : seat[0] + 2, seat[1] : seat[1] + 2].flatten()
        adjacents = np.delete(adjacents, 0)

    # Bottom-Right Corner (special case)
    elif seat[0] == grid.shape[0] - 1 and seat[1] == grid.shape[1] - 1:
        adjacents = grid[seat[0] - 1 : seat[0] + 2, seat[1] - 1 : seat[1] + 2].flatten()
        adjacents = np.delete(adjacents, 3)

    # Seat in Top-Most Row (special case)
    elif seat[0] == 0:
        adjacents = grid[seat[0] : seat[0] + 2, seat[1] - 1 : seat[1] + 2].flatten()
        adjacents = np.delete(adjacents, 1)

    # Seat in Left-Most Column (special case)
    elif seat[1] == 0:
        adjacents = grid[seat[0] - 1 : seat[0] + 2, seat[1] : seat[1] + 2].flatten()
        adjacents = np.delete(adjacents, 2)

    # Seat in Right-Most Column (special case)
    elif seat[1] == grid.shape[1] - 1:
        adjacents = grid[seat[0] - 1 : seat[0] + 2, seat[1] - 1 : seat[1] + 2].flatten()
        adjacents = np.delete(adjacents, 3)

    # Inner Seats
    else:
        adjacents = grid[seat[0] - 1 : seat[0] + 2, seat[1] - 1 : seat[1] + 2].flatten()
        adjacents = np.delete(adjacents, 4)

    return adjacents


def apply_rules(arr: np.array):

    """
    Per the problem statement:
    ---------------------------

    Apply the following rules to every seat SIMULTANEOUSLY:
    - If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    - If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    - Otherwise, the seat's state does not change.

    Return an array of the new grid / state after all the rules have been applied.
    """
    data_array = arr.copy()

    new_state = np.zeros(shape=data_array.shape, dtype="<U1")
    new_state[data_array == "."] = "."
    for i, row in enumerate(data_array):
        for j, seat in enumerate(row):
            adjacents = get_adjacents([i, j], data_array)
            num_occ = (adjacents == "#").sum()
            if data_array[i, j] == "L" and num_occ == 0:
                new_state[i, j] = "#"
            elif data_array[i, j] == "#" and num_occ >= 4:
                new_state[i, j] = "L"
            else:
                new_state[i, j] = data_array[i, j]

    return new_state


if __name__ == "__main__":

    data_array = read_data("input.txt")

    print(
        "Calculating...this isn't the quickest solution (but shouldn't take more than 5-10 seconds)...\n\n"
    )
    for i in range(200):
        new_array = apply_rules(data_array)
        if not np.array_equal(new_array, data_array):
            data_array = new_array
        else:
            print(
                f'Converged! The number of occupied seats after convergence is {(new_array=="#").sum()}.'
            )
            break
