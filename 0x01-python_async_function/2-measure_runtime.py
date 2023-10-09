#!/usr/bin/env python3
"""measure_time module"""

import asyncio
import time

# Local
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n when
    called with n and max_delay and returns the total_time / n.

    Args:
        n (int): Number of times to spawn wait_random in wait_n.
        max_delay (int): Max delay passed to wait_random in wait_n.

    Returns:
        float: The quotient of total time / n.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start

    return elapsed / n
