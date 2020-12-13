"""
Part 1 of https://adventofcode.com/2020/day/5

As a sanity check, look through your list of boarding passes.
What is the highest seat ID on a boarding pass?
"""
import numpy as np


def read_data(filename: str) -> list:
    with open(filename, "r") as f:
        data = f.read().split("\n")
    return data


def split_list(li):
    """Split a given list into a right half and left half."""
    half = len(li) // 2
    return li[:half], li[half:]


def get_seat_id(seat: str) -> int:

    """
    Find seat id of a given boarding pass, following the airline's
    'binary space partitioning' rules.
    """

    key = {"F": 0, "B": 1, "L": 0, "R": 1}

    row = list(range(128))
    col = list(range(8))
    for i, char in enumerate(seat):
        if i < 7:
            row = split_list(row)[key[char]]
        else:
            col = split_list(col)[key[char]]

    return row[0] * 8 + col[0]


if __name__ == "__main__":
    seat_ids = []
    for bp in read_data("input.txt"):
        si = get_seat_id(bp)
        seat_ids.append(si)

    print(f"Solution: The highest seat id is {np.max(seat_ids)}")
