#!/usr/bin/env python3
"""
Contains a class LIFOCache that inherits from BaseCaching
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    A caching system
    Implements the LIFO algorithm
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        Adds an item in the cache
        If the number of items is higher that BaseCaching.MAX_ITEMS, discard
        the first element
        """
        if len(self.cache_data.keys()) >= super().MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            self.cache_data.pop(last_key)
            print(f'DISCARD: {last_key}')
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item by key
        """
        return self.cache_data.get(key)
