#!/usr/bin/env python3
"""8-make_multiplier: has function make_multiplier"""


def make_multiplier(multiplier: float) -> callable[[float], float]:
    """returns a function that multiplies the float wit a multiplier"""
    def multiplier_(num: float) -> float:
        """multiplies the float with a multiplier"""
        return num * multiplier
    return multiplier_
