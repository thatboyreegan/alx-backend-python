#!/usr/bin/env python3
"""1-concurrent_coroutines.p module has wait_n coroutine"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawns a coroutine n times
    Args:
        n (int): number of times to spa the coroutine
        max_delay(int):endpoint passed to the random method in the spawned
        coroutine

    Return:
        List(float): list of all the delays in ascending order
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
