#!/usr/bin/env python3
"""make_multiplier module"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiplier functions factory. Creates a function that multiplies
    a float with multiplier.

    Args:
        multiplier (float) - Number to generate a multiplier function.

    Returns:
        Callable: A function that can be called with a float and returns
            the product of the float and multiplier.
    """

    def multiply(num: float) -> float:
        """Multiply num with multiplier."""
        return num * multiplier

    return multiply
