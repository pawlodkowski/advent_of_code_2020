"""
Part 1 of https://adventofcode.com/2020/day/8
"""

import re
from typing import List, Tuple


def read_data(filename: str) -> list:
    with open(filename, "r") as f:
        data = f.read().split("\n")
    return data


def get_acc_val(data: List) -> Tuple[int, bool]:
    """
    Get the accumulator value for the given dataset.
    Also return whether or not this value was accumulated prior
    to causing an infinite loop (i.e. whether the program "exploded").
    If exploded=False, this means that the program successfully reached
    the end of the instructions and terminated naturally.
    """
    idx = 0
    acc = 0
    visits = []
    exploded = False
    while True:
        try:
            visits.append(idx)
            move = data[idx]
            action = re.findall("[a-z]+", move)[0]
            amount = int(re.findall("\s(.+)", move)[0])
            if action == "jmp":
                idx += amount
            if action == "acc":
                acc += amount
                idx += 1
            if action == "nop":
                idx += 1
            if idx in visits:
                exploded = True
                break
        except IndexError:
            # if idx is larger than the length of data,
            # i.e, the program has successfully run through to the end
            break
    return acc, exploded


if __name__ == "__main__":
    data = read_data("input.txt")
    acc, _ = get_acc_val(data)
    print(
        f"Immediately before any instruction is executed a second time, the accumulator has a value of {acc}."
    )
