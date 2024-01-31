#!/usr/bin/env python3
""" BaseCaching module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """basic caching system"""
    def put(self, key, item):
        """Add an item to the cache."""
        if key and item:
            self.cache_data[key] = item
        else:
            pass

    def get(self, key):
        """Get an item from the cache."""
        if key and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
