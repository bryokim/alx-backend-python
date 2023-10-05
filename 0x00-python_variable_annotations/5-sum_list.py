#!/usr/bin/env python3
"""sum_list module"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Find sum of a list of floats.

    Args:
        input_list (List[float]) - List of floats.

    Return:
        float : Sum of the floats.
    """
    sum: float = 0
    for value in input_list:
        sum += value

    return sum
