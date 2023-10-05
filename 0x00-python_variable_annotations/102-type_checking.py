#!/usr/bin/env python3
"""zoom_array module"""

from typing import List, SupportsIndex


def zoom_array(lst: List, factor: SupportsIndex = 2) -> List:
    """Zoom an array by factor"""
    zoomed_in = [
        item
        for item in lst
        for _ in range(factor)
    ]

    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
