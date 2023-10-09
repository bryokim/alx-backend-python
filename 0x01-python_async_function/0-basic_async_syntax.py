#!/usr/bin/env python3
"""wait_random module"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait  for a random number of seconds and return
    the time waited.

    Args:
        max_delay (int, optional): Maximum delay time. Defaults to 10.

    Returns:
        float: Time spent waiting.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
