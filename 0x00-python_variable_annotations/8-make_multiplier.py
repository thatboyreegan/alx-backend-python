#!/usr/bin/env python3
"""8-make_multiplier: has function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies the float wit a multiplier"""
    def multiplier_(num: float) -> float:
        """multiplies the float with a multiplier"""
        return num * multiplier
    return multiplier_
