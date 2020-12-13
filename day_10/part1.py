"""
Part 1 of https://adventofcode.com/2020/day/10
"""

import pandas as pd


def read_data(filename: str) -> list:
    """
    Read in data, making sure everything is numerical and sorted.

    Also, per the problem statement:

        - a joltage value of zero should be inserted at the beginning of the list
        (i.e. effective joltage rating of the starting outlet); and

        - a joltage value of 3 higher than the maximum value should be inserted at
        the end of the list (i.e. the device's built-in adapter is always 3 higher
        than the highest afapter in the bag).
    """
    with open(filename, "r") as f:
        data = f.read().split("\n")
    data = sorted([int(i) for i in data])
    data.insert(0, 0)  # extra one in the beginning from 0->1
    data.append(data[-1] + 3)  # extra three at the end for max + 3
    return data


if __name__ == "__main__":

    data = read_data("input.txt")
    df = pd.DataFrame(data, columns=["jolts"])
    df["jolts_diff"] = df["jolts"] - df["jolts"].shift(1)
    result = (df["jolts_diff"] == 1).sum() * (df["jolts_diff"] == 3).sum()
    print(
        f"Solution: the number of 1-jolt differences multiplied by the number of 3-jolt differences is {result}."
    )
