#!/usr/bin/env python3
"""Floor module"""


def floor(n: float) -> int:
    """Returns floor of a float.

    Args:
        n (float) - Number to floor.

    Returns:
        int : Floor of n.
    """
    return n.__floor__()
