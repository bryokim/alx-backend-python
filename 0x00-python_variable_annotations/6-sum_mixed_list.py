#!/usr/bin/env python3
"""sum_mixed_list module"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Find sum of a mixed list of both integers and floats.

    Args:
        mxd_lst (List[int | float]) - List of both integers and floats.

    Returns:
        float: Sum of the value in mxd_lst as a float.
    """
    sum: float = 0

    for value in mxd_lst:
        sum += value

    return sum
