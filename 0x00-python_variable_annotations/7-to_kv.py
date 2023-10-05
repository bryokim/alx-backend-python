#!/usr/bin/env python3
"""to_kv module"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns tuple of k and square of v.

    Args:
        k (str) - A string.
        v (int | float) - An integer or float.

    Returns:
        tuple : Tuple of k and square of v.
    """
    return (k, v**2)
