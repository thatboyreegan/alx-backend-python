#!/usr/bin/env python3
"""100-safe_first_element.py: has function safe_first_element"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns any type or nonetype"""
    if lst:
        return lst[0]
    else:
        return None
