#!/usr/bin/env python3
"""2-measure_runtime has the coroutine measure_time"""

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measures the total execution time fora coroutine

    Args:
        n (int): number to use as a denominator in finding the quotient
        max_delay(int):endpoint passed to the random method in the spawned
        coroutine

    Returns:
        Float: time of execution
    """
    beginning = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - beginning

    return total_time / n
