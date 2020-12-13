"""
Part 2 of https://adventofcode.com/2020/day/9
"""

import part1
import numpy as np

INVALID = 1309761972  # Answer from Part1


def find_sum(data):
    for i in range(len(data)):
        for j in range(0, i + 1):
            moving_slice = data[j:i]
            if sum(moving_slice) == INVALID:
                return np.min(moving_slice) + np.max(moving_slice)
    return 0


if __name__ == "__main__":
    data = [int(i) for i in part1.read_data("input.txt")]
    print(
        f"Solution: The sum of the smallest and largest numbers in a contiguous range that add up to Part 1's answer is {find_sum(data)}."
    )
