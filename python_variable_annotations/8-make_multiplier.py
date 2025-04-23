#!/usr/bin/env python3
"""Function - Make a multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a function that multiplies a number by the multiplier."""
    def multiplier_func(x: float) -> float:
        """Multiply a number by the multiplier."""
        return x * multiplier
    return multiplier_func
