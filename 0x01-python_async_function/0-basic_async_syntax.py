#!/usr/bin/env python3
"""0-basic_async_syntax module has coroutine named wait_random"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random delay between 0 and the provided seconds

    Args:
        max_delay(int) : endpoint for random.uniform

    Returns:
        (float): random delay in seconds that he coroutine has to await
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
