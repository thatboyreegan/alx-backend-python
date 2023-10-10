#!/usr/bin/env python3
"""1-async_comprehension has the async_comprehension coroutine"""

import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Returns 10 random number collected using an async comprehensing over t
    he async_generator coroutine
    """
    result = [i async for i in async_generator()]
    return result
