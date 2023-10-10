#!/usr/bin/env python3
"""0-async_generator has the coroutine async_generator"""

import asyncio
from typing import List
import random


async def async_generator() -> float:
    """
    takes no arguments and generates a random number
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def main() -> List[float]:
    """
    wrapper coroutine
    """
    result = [i async for i in async_generator()]
    return result
