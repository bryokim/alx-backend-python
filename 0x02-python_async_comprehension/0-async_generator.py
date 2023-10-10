#!/usr/bin/env python3
"""async_generator module"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Loops 10 times yielding a random number between 0 and 10
    after a 1 second wait.

    Returns:
        AsyncGenerator[float, None]: Asynchronous generator.

    Yields:
        Iterator[AsyncGenerator[float, None]]: An asynchronous iterator.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
