#!/usr/bin/env python3
"""calculate indexes"""


def index_range(page: int, page_size: int) -> tuple:
    """ start and end index derivation"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
