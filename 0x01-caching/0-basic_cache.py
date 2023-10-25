#!/usr/bin/env python3
"""
Contains a class BasicCache, that inherits from BaseCaching
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    A caching system that has no limit
    """

    def put(self, key, item):
        """
        Adds an item to the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets the cache item by key
        """
        return self.cache_data.get(key)
