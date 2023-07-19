#!/usr/bin/python3
"""Using redis to create a cache"""



import uuid
import redis


class Cache:
    """This is a Cache using redis
    """

    def __init__(self):
        """Intialization for cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        """A store method"""
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key
