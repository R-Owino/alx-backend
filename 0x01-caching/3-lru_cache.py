#!/usr/bin/env python3
"""
Contains a class LRUCache that inherits from BaseCaching
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    A caching system
    Implements the LRU algorithm
    """

    def __init__(self):
        super().__init__()
        self.mem_cache = {}
        self.counter = 0

    def put(self, key, item):
        """
        Adds an item in the cache
        If the number of items is higher that BaseCaching.MAX_ITEMS, discard
        the first element
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    min_val = min(self.mem_cache, key=self.mem_cache.get)
                    del self.cache_data[min_val]
                    del self.mem_cache[min_val]
                    print(f"DISCARD: {min_val}")
                self.cache_data[key] = item

            self.mem_cache[key] = self.counter
            self.counter += 1

        elif key is None or item is None:
            return

    def get(self, key):
        """
        Gets an item by key
        """
        self.mem_cache[key] = self.counter
        self.counter += 1
        return self.cache_data.get(key)
