#!/usr/bin/env python3
""" Complex types - mixed list """
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """taes in a mix of floats and integers and returns the sum as a float """
    return sum(mxd_lst)
