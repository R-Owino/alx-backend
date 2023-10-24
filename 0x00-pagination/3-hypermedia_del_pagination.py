#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a dictionary with information for pagination.

        Args:
            index (int, optional): The current start index of the return page.
                Defaults to None.
            page_size (int, optional): The current page size. Defaults to 10.

        Returns:
            dict: A dictionary with pagination information.
        """

        if index is None:
            index = 0

        # Ensure that index is in a valid range
        assert 0 <= index < len(self.dataset()), "Index is out of range"

        # Calculate the current start index and next index
        start_index = index
        next_index = min(start_index + page_size, len(self.dataset()))

        # Get the actual page of data
        data = self.dataset()[start_index:next_index]

        return {
            "index": start_index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }
