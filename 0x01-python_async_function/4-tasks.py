#!/usr/bin/env python3
"""task_wait_n module"""

import asyncio
from typing import List

# Local
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Max delay passed to task_wait_random.

    Returns:
        List[float]: List of all the delays in ascending order, that is,
            as the tasks were completed.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]

    return delays
