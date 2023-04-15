#!/usr/bin/env python3
"""
This module provides a function for calculating the start and end indices for
a given page and page size, using 1-indexing.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end indices for the specified page and page size.

    Args:
        page (int): The 1-indexed page number to calculate the indices for.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indices for
the specified page and page size.

    Raises:
        ValueError: If either page or page_size is not a positive integer.
    """
    if not isinstance(page, int) or page < 1:
        raise ValueError("page must be a positive integer")
    if not isinstance(page_size, int) or page_size < 1:
        raise ValueError("page_size must be a positive integer")
    
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)

