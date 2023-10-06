#!/usr/bin/env python3
"""5-sum_list: has the function sum_list"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """takes a list of floats and returns their sum as float
    Args:
        input_list (list[float]) - list of floats

    Return:
        Float: sum of the arguments"""
    sum: float = 0
    for item in input_list:
        sum += item
    return sum
