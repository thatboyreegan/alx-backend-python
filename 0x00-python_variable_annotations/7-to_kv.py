#!/usr/bin/env python3
"""7-to_kv.py: has the function to_kv"""


def to_kv(k: str, v: int | float) -> tuple[str, float]:
    """takes a string of int/float as arguments and returns a tuple"""
    return (k, v * v)
