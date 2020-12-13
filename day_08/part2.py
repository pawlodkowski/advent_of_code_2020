"""
Part 2 of https://adventofcode.com/2020/day/8
"""

import part1
import re
from typing import List


def fix_program(data: List) -> int:
    """
    Fix the program so that it terminates normally by
    changing exactly one jmp (to nop) or nop (to jmp).

    Find the tweaked version of the datathat makes the program
    run successfully without "exploding" (i.e. landing in an infinite loop),
    and return the accumulator value of that tweaked version
    """
    for idx, move in enumerate(data):
        datacopy = data.copy()
        action = re.findall("[a-z]+", move)[0]
        amount = int(re.findall("\s(.+)", move)[0])
        if action == "jmp":
            move = re.sub(action, "nop", move)
            datacopy[idx] = move
        if action == "nop":
            move = re.sub(action, "nop", move)
            datacopy[idx] = move

        acc, exploded = part1.get_acc_val(datacopy)

        if exploded:
            pass
        else:
            return acc


if __name__ == "__main__":
    data = part1.read_data("input.txt")
    result = fix_program(data)
    print(
        f"The value of the accumulator after the program terminates normally is {result}."
    )
