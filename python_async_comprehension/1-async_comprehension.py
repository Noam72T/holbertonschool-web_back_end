#!/usr/bin/env python3
""" Async comprenhesion gen """
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
        Collects 10 random numbers using an async comprehension.

        Args:
            void

        Return:
            List[float]: A list of 10 random floats between 0 and 10.
    """
    return ([i async for i in async_generator()])
