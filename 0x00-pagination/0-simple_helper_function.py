#!/usr/bin/env python3
"""
This module provides a function for calculating the start and end indices for
a given page and page size, using 1-indexing.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end indices for the specified page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)

