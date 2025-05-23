#!/usr/bin/env python3
"""
Module for measuring runtime of concurrent coroutines
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for
    wait_n(n, max_delay) and returns total_time/n

    Args:
        n (int): Number of coroutines to run
        max_delay (int): Maximum delay in seconds

    Returns:
        float: Average execution time per coroutine
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    return (end_time - start_time) / n
