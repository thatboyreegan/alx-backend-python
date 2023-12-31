#!/usr/bin/env python3
"""6-sum_mxd_list: has the function sum_mxd_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes a list and returns sum of elements as float

    Args:
        input_list (list[float | int]) - list of floats and integers

    Return:
        Float: sum of the arguments"""
    sum: float = 0
    for item in mxd_lst:
        sum += item
    return sum
