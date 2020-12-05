"""
Your seat wasn't at the very front or back, though;
the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?
"""

import part1
import numpy as np


def missing_elements(sorted_list):
    """Find missing elements in a list of consecutive integers, given that the list is sorted."""
    return [
        x for x in range(sorted_list[0], sorted_list[-1] + 1) if x not in sorted_list
    ]


if __name__ == "__main__":
    seat_ids = []
    for bp in part1.read_data("input.txt"):
        si = part1.get_seat_id(bp)
        seat_ids.append(si)

    print(f"Solution: Your Seat Id is {missing_elements(np.sort(seat_ids))[0]}")
