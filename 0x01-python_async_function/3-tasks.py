#!/usr/bin/env python3
"""3-tasks has the task_wait_random function"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    takes an integer and returns an asyncio.Task

    Args:
        max_delay(int): value to pass to the task

    Return:
        asyncio.Task: created task
    """
    return asyncio.create_task(wait_random(max_delay))
