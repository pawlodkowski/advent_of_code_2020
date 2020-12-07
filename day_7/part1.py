"""
Part 1 of https://adventofcode.com/2020/day/7
"""

from colordict import ColorDict
import collections

MY_BAG_COLOR = "shiny gold"


def read_data(filename: str) -> list:
    with open(filename, "r") as f:
        data = f.read().split("\n")
    return data


def get_parent_containers(color_dict: collections.defaultdict, color: str) -> set:
    """
    Given an inverted color dictionary (i.e. child->parents relationship) and
    a starting color (e.g. 'shiny gold'), recursively find all parents up the 'family tree',
    e.g. parents, parents of parents, parents of parents of parents, etc. until all paths
    are traversed.

    Returns
    --------
    Set (i.e. no duplicates) of all of the bag colors that eventually contain at least
    one bag of the given starting color.
    """
    containers = color_dict[color]
    containers_set = set(containers)

    for ctr in containers:
        next_containers = get_parent_containers(color_dict, ctr)
        containers_set = containers_set.union(next_containers)

    return containers_set


if __name__ == "__main__":
    data = read_data("input.txt")
    cd = ColorDict(data, inverted=True, include_counts=False)
    result = get_parent_containers(cd.dict, MY_BAG_COLOR)
    print(
        f"Solution: {len(result)} bag colors can eventually contain at least one {MY_BAG_COLOR} bag."
    )
