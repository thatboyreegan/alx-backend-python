#!/usr/bin/env python3
"""has function safely_get_value"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None]
) -> Union[Any, T]:
    """returns any type or type T"""
    if key in dct:
        return dct[key]
    else:
        return default
