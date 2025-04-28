#!/usr/bin/env python3
"""
Module for creating an async generator that yields random numbers
"""

import asyncio
import random
from async_generator import async_generator
from typing import List


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension.

    The coroutine uses an async comprehension over async_generator
    to collect 10 random floats between 0 and 10 into a list.

    Returns:
        List[float]: A list of 10 random floats between 0 and 10.
    """
    return [i async for i in async_generator()]
