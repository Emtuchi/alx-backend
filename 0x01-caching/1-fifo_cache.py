#!/usr/bin/env python3
""" BaseCaching module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """delete first key, if a condition is met"""
    def __init__(self):
        """ Initialize class instance. """
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache."""
        if key and item:
            self.cache_data[key] = item
        else:
            pass

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = sorted(self.cache_data)[0]
            self.cache_data.pop(discarded_key)
            print('DISCARD: {}'.format(discarded_key))

    def get(self, key):
        """Get an item from the cache."""
        if key and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
