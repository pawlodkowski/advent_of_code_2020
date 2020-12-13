"""
Part 1 of https://adventofcode.com/2020/day/9
"""


def read_data(filename: str) -> list:
    with open(filename, "r") as f:
        data = f.read().split("\n")
    return data


def sum_to_n(n, options):
    """
    Helper function adapted from Day 1 :)
    """
    try:
        for num in options:
            complement = n - num
            if complement in options:
                first = num
                second = complement
                break

        return first, second
    except UnboundLocalError:
        return False


if __name__ == "__main__":

    data = [int(i) for i in read_data("input.txt")]

    for i, num in enumerate(data):
        prev25 = data[i - 25 : i]
        if prev25:
            if not sum_to_n(num, prev25):
                print(
                    f"Solution: The first number that is not the sum of any two of the 25 numbers before it is {num}."
                )
