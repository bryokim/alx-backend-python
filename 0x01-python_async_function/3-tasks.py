#!/usr/bin/env python3
"""task_wait_random module"""

import asyncio

# Local
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns an asyncio Task with the coroutine wait_random.

    Args:
        max_delay (int): Maximum delay time.

    Returns:
        asyncio.Task: An asyncio Task with the coroutine wait_random
    """
    return asyncio.create_task(wait_random(max_delay))
