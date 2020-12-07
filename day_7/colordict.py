"""
Module for the Color Dictionary class, a flexible dictionary-like data 
structure used to solve the Advent of Code 2020 Day 7 problem using recursion.
"""

import collections


def clean_text(text: str) -> str:
    """
    Helper function for cleaning text during the generation of the
    primary data structure for this problem (the "color dictionary").

    Pretty manual (could be improved with RegEx), but it does the job in
    removing:
        - the word "bag" or "bags",
        - periods (.),
        - extra white-space
    """
    return text.replace(" bags", "").replace(" bag", "").replace(".", "").strip()


class ColorDict:

    """
    Custom class for a "color dictionary", i.e. a data structure that maps a bag color (key) to
    a list of all bag colors (value) in which the bag color (key) must be contained.

    For example:
    --------------
    'vibrant plum': ['dim lavender', 'muted turquoise', 'wavy blue', 'dull tan'] ...

    ... would mean that a 'dim lavender' bag must contain at least one 'vibrant plum' bag,
    a 'muted turquoise' bag must contain at least one 'vibrant plum' bag, etc.
    This can be thought of as a "child->parents" relationship (with multiple parents).

    Inverted mode
    --------------
    If the default "inverted" mode is NOT selected (i.e. False), the dictionary has the same
    structure, but the relationship is inverted. Taking the same example as above:

    'vibrant plum': ['dim lavender', 'muted turquoise', 'wavy blue', 'dull tan'] ...

    ... would now mean that a 'vibrant plum' must contain at least one 'dim lavender' bag,
    a 'vibrant plum' bag must contains at least one 'muted turquoise' bag, etc.
    This can be thought of as a "parent->children" relationship.

    Include counts
    --------------
    If the "include_counts" mode is switched to True, the colors (regardless of whether they are keys
    or values) will include the number / count. For example:

    'dark coral': ['5 dull aqua', '5 plaid green', '2 posh bronze'] ...

    ... would mean that -- assuming "inverted" mode is False -- a 'dark coral' bag must contain
    5 'dull aqua' bags, 5 'plaid green' bags, and 2 'posh bronze' bags.
    """

    def __init__(self, data: list, inverted=True, include_counts=False):
        self.data = data
        self.inverted = inverted
        self.include_counts = include_counts
        self.dict = self.gen_color_dict()

    def gen_color_dict(self) -> collections.defaultdict:

        """
        Generate the actual "color dictionary" data structure based on the specified parameters.

        Returns
        --------------
        A defaultdict (from the collections library) for all the colors in the data file
        according to the specified parameters. The defaultdict was chosen (as opposed to
        a normal python dictionary) for easier syntax when dealing with potential key errors.
        """

        color_dict = collections.defaultdict(list)
        for line in self.data:
            left, right = line.split(" contain ")
            container = clean_text(left)

            for contents in right.split(","):

                if not self.include_counts:
                    contained = clean_text(contents[2:])
                    if self.inverted:
                        color_dict[contained].append(container)
                    else:
                        color_dict[container].append(contained)

                else:
                    contained = clean_text(contents)
                    if self.inverted:
                        color_dict[contained].append(container)
                    else:
                        color_dict[container].append(contained)

        return color_dict