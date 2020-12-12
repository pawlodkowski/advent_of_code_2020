"""
Part 1 of https://adventofcode.com/2020/day/12
"""


# TO-DO: Is it possible to contain the navigation information in a single data structure?
CARDINALS = {"E": (1, 0), "S": (0, -1), "W": (-1, 0), "N": (0, 1)}
BEARINGS = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # maps to current bearing


def read_data(filename: str) -> list:
    with open(filename, "r") as f:
        data = f.read().split("\n")
    return data


def chart_path(start_location: tuple, start_bearing: int, instructions: list) -> tuple:
    """
    Given starting coordinates (e.g. (0,0)) and initial bearing (e.g. 0)
    and a list of navigation instructions, chart the path of the ship
    and return the final coordinates of the ship after executing all the instructions.

    Here is a key for the current bearing meaning:

        0 <-> 'E'
        1 <-> 'S'
        2 <-> 'W'
        3 <-> 'N'

    """

    current_location = start_location
    current_bearing = start_bearing

    for command in instructions:
        action = command[0]
        value = int(command[1:])

        no_rotation = action == "F" or action in CARDINALS

        if no_rotation:

            if action == "F":

                change_x = BEARINGS[current_bearing][0] * value
                change_y = BEARINGS[current_bearing][1] * value

            else:
                change_x = CARDINALS[action][0] * value
                change_y = CARDINALS[action][1] * value

            current_location = (
                current_location[0] + change_x,
                current_location[1] + change_y,
            )

        else:

            if action == "R":

                current_bearing = (current_bearing + (int(value / 90))) % 4
                # modulus 4 is to reset the rotation back to zero so the numbers cycle

            else:

                current_bearing = (current_bearing - (int(value // 90))) % 4

    return current_location


if __name__ == "__main__":
    data = read_data("input.txt")
    final = chart_path((0, 0), 0, data)
    print(
        f"Solution: the final manhattan distance from the ship's starting point is {abs(final[0]) + abs(final[1])}."
    )
