#!/usr/bin/env python3
"""
Contains a class FIFOCache that inherits from BaseCaching
"""

BaseCaching = __import__('BaseClass').BaseCaching


class FIFOCache(BaseCaching):
    """
    A caching system
    Implements the FIFO algorithm
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Adds an item in the cache
        If the number of items is higher that BaseCaching.MAX_ITEMS, discard
        the first element
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data.keys()) > super().MAX_ITEMS:
                last_key = list(self.cache_data.keys())[0]
                self.cache_data.pop(last_key)
                print(f'DISCARD: {last_key}')

    def get(self, key):
        """
        Gets an item by key
        """
        return self.cache_data.get(key)
