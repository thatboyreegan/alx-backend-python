#!/usr/bin/env python3
"""4-tasks has the coroutine task_wait_n"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawns a coroutine n times
    Args:
        n (int): number of times to spawn the coroutine
        max_delay(int):endpoint passed to the random method in the spawned
        coroutine

    Return:
        List(float): list of all the delays in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
