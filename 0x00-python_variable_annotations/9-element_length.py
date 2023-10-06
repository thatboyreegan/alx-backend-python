#!/usr/bin/env python3
"""9-element_length.py: has function element_length"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of type sequence or int"""
    return [(i, len(i)) for i in lst]
