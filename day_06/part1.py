"""
Part 1 of https://adventofcode.com/2020/day/6
"""


def read_data(filename: str) -> list:
    with open(filename, "r") as f:
        data = f.read().split("\n\n")
    return data


if __name__ == "__main__":
    groups = [s for s in read_data("input.txt")]

    unique_yes = 0
    for g in groups:
        unique = "".join(set(g.replace("\n", "")))
        unique_yes += len(unique)

    print(
        f'Solution: the sum of the number of questions to which ANYONE in the same group answered "yes" is {unique_yes}.'
    )
