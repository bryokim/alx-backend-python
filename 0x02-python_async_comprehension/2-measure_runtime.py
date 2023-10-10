#!/usr/bin/env python3
"""measure_time module"""

import asyncio
import time

# Local
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Measures total time taken to run async_comprehension four times.

    Returns:
        float: Number of seconds taken.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    elapsed = time.perf_counter() - start

    return elapsed
