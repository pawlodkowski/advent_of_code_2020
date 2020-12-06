"""
Part 2 of https://adventofcode.com/2020/day/6
"""

import part1


if __name__ == "__main__":
    data = [s for s in part1.read_data("input.txt")]
    groups = [g.split("\n") for g in data]

    all_common = 0
    for i in groups:
        first = set(i[0])
        common = set(first).intersection(*i)
        all_common += len(common)

    print(
        f'Solution: the sum of the number of questions to which EVERYONE in the same group answered "yes" is {all_common}.'
    )
