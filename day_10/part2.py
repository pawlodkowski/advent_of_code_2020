"""
Part 2 of https://adventofcode.com/2020/day/10
"""

import part1


def get_cumulative_path_possibilities(data: list) -> list:
    """
    Function to solve the problem for part 2:

        'What is the total number of distinct ways you can arrange the adapters
        to connect the charging outlet to your device?'

    Reasoning:
    ----------

    If a chain of numbers are perfectly consecutive, e.g. 4, 5, 6, 7 then the number of possible paths required
    to get from the first number (4) to the last number (7) -- according to the constraints of the problem --
    is the sum of the possible paths of getting to each of the previous 3. In other words, this would be a perfect
    Tribonacci sequence (i.e. a generalization of the Fibonacci sequence where each term is the sum of the
    3 preceding terms).

    HOWEVER, our pattern gets complicated if there are breaks / the sequence is NOT consecutive (e.g. 1, 4, 5, 6).
    So, after observing the pattern on the example data input and doing some counting by hand, I was able to formulate
    a more general rule, i.e.:

        The number of possible paths to get to a number x is the sum of possibible paths of getting to the previous
        numbers that are WITHIN RANGE of x, meaning that their values are greater than or equal to x - 3.

    Parameters:
    -----------


    """

    path_possibilities = [0] * len(data)
    path_possibilities[
        0
    ] = 1  # there is exactly one possible way to get from the first number to itself.

    for i, current_val in enumerate(data):

        for j in range(i - 3, i):

            val_from_j_nums_ago = data[j]
            within_range = current_val - val_from_j_nums_ago <= 3

            if within_range:
                path_possibilities[i] += path_possibilities[j]

            else:
                pass

    return path_possibilities


if __name__ == "__main__":
    data = part1.read_data("input.txt")
    result = get_cumulative_path_possibilities(data)[-1]
    print(
        f"Solution: the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device is {result}."
    )
