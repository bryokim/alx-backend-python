#!/usr/bin/env python3
"""safe_first_element module"""

from typing import Any, Sequence, Union


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return first element if available or none"""

    if lst:
        return lst[0]
    else:
        return None
