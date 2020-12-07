"""
Part 2 of https://adventofcode.com/2020/day/7
"""

import collections

import part1
from colordict import ColorDict

MY_BAG_COLOR = "shiny gold"


def count_single_level(num_container, num_children):
    """
    Helper function to calculate the number of children bags
    for a single layer deep, i.e. ignoring the descendents of the
    children bags.

    Example
    --------
    A single shiny gold bag must contain 1 dark olive bag
    (and the 7 bags within it) plus 2 vibrant plum bags
    (and the 11 bags within each of those):
    1 + 1*7 + 2 + 2*11 = 32 bags!
    """
    return num_container + num_container * num_children


def count_descendents(color_dict, color: str) -> int:
    """
    Given a non-inverted color dictionary (i.e. parent->children relationship) and
    a starting color (e.g. 'shiny gold'), recursively find all children down the 'family tree',
    e.g. children, children of children, children of children of children, etc. until all paths
    are traversed.

    Returns
    --------
    Count of all of the bag colors that eventually must be contained within the bag
    of the given starting color.
    """
    count = 0

    for content in color_dict[color]:
        num_contents = content.split()[0]
        if num_contents == "no":
            num = 0
        else:
            num = int(num_contents)
        contained_color = content.split(maxsplit=1)[1]
        new_count = count_single_level(
            num, count_descendents(color_dict, contained_color)
        )
        count += new_count
    return count


if __name__ == "__main__":
    data = part1.read_data("input.txt")
    cd = ColorDict(data, inverted=False, include_counts=True)
    result = count_descendents(cd.dict, MY_BAG_COLOR)
    print(
        f"Solution: {result} individual bags are required inside a single {MY_BAG_COLOR} bag."
    )
