#!/usr/bin/env python3
"""2-measure_runtime has the coroutine measure_runtime"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    executes async_comprehension four times in parallel using asyncio.gather
    then measuring the total run time and returning it
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    total_runtime = time.perf_counter() - start
    return total_runtime
