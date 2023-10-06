#!/usr/bin/env python3
"""7-to_kv.py: has the function to_kv"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes a string of int/float as arguments and returns a tuple"""
    return (k, v ** 2)
