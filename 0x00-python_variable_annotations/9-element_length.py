#!/usr/bin/env python3
"""element_length module"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Find the length of each element in a list."""

    return [(i, len(i)) for i in lst]
