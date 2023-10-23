#!/usr/bin/env python3
"""
Contains a class server, extends from task 0
"""

import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """
        Calculate the start and end indexes for a given page and page size.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            tuple: contains the start and end indexes for the specified page
        """
        if page <= 0 or page_size <= 0:
            raise ValueError("Page and page_size must be positive integers.")

        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return start_index, end_index

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Extends index_range to get the pages

        Args:
            page (int): The page number
            page_size (int): Number of items per page

        Returns:
            A list of the paginated data
            Otherwise empty list if input args are out of range
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()

        try:
            start = (page - 1) * page_size
            end = start + page_size
            return data[start:end]
        except IndexError:
            return []
