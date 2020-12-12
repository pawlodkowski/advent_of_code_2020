"""
Unit tests that were useful during the development of the code.

Run with `pytest`.
"""

from part1 import get_adjacents, apply_rules
import numpy as np

test = np.random.rand(5, 5)


def test_upper_left_corner():
    """zero case for seat [0,0], i.e. upper left corner"""
    np.testing.assert_array_equal(
        np.delete(test[0:2, 0:2].flatten(), 0), get_adjacents([0, 0], test)
    )


def test_top_row():
    """zero case for seat [0,2], i.e. somewhere in top-most row"""
    np.testing.assert_array_equal(
        np.delete(test[0:2, 1:4].flatten(), 1), get_adjacents([0, 2], test)
    )


def test_top_right_corner():
    """zero case for seat [0,4], i.e. top right corner"""
    np.testing.assert_array_equal(
        np.delete(test[0:2, 3:6].flatten(), 1), get_adjacents([0, 4], test)
    )


def test_right_col():
    """zero case for seat [2,4], i.e. somewhere in right-most col"""
    np.testing.assert_array_equal(
        np.delete(test[1:4, 3:6].flatten(), 3), get_adjacents([2, 4], test)
    )


def test_left_col():
    """zero case for seat [2,0], i.e. somewhere in left-most col"""
    np.testing.assert_array_equal(
        np.delete(test[1:4, 0:2].flatten(), 2), get_adjacents([2, 0], test)
    )


def test_bottom_left_corner():
    """zero case for seat [4,0], i.e. bottom-left corner"""
    np.testing.assert_array_equal(
        np.delete(test[3:6, 0:2].flatten(), 2), get_adjacents([4, 0], test)
    )
