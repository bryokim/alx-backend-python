#!/usr/bin/env python3
"""async_comprehension module"""

from typing import List

# Local
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using an async comprehension
    over async_generator then returns the 10 numbers.

    Returns:
        List[float]: List of floats produced by async_generator.
    """
    return [i async for i in async_generator()]
