#!/usr/bin/env python3

"""
Contains a class LFUCache that inherits from BaseCaching
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    A caching system
    Implements the LFU algorithm
    """
    def __init__(self):
        super().__init__()
        self.lfu_keys = {}
        self.count = 0

    def put(self, key, item):
        """
        Adds an item in the cache
        If the number of items is higher that BaseCaching.MAX_ITEMS:
            - discard the least frequency used item
            - if more than 1 item is to discarded, use LRU algorithm to discard
            only the least recently used
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= super().MAX_ITEMS:
                    min_value = min(self.lfu_keys.values())
                    min_keys = [k for k in self.lfu_keys
                                if self.lfu_keys[k] == min_value]
                    if len(min_keys) > 1:
                        min_keys = sorted(min_keys)
                        del self.cache_data[min_keys[0]]
                        del self.lfu_keys[min_keys[0]]
                        print("DISCARD: {}".format(min_keys[0]))
        self.cache_data[key] = item
        self.lfu_keys[key] = 0

    def get(self, key):
        """
        Gets an item by key
        """
        self.lfu_keys[key] += 1
        return self.cache_data[key]
