#!/usr/bin/env python3
"""wait_n module"""

import asyncio
from typing import List

# Local
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Max delay passed to wait_random.

    Returns:
        List[float]: List of all the delays in ascending order, that is,
            as the tasks were completed.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]

    return delays
