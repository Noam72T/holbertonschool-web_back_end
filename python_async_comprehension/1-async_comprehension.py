#!/usr/bin/env python3
"""
Module for creating an async generator that yields random numbers
"""

import asyncio
import random


async def async_generator():
    """
        Asynchronous generator that yields a random number between 0 and 10
        every second for 10 seconds.
 """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)


async def async_comprehension():
    return [num async for num in async_generator()]
