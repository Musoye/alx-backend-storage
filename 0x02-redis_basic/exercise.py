#!/usr/bin/python3
"""Using redis to create a cache"""


import redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''Decorator for counting'''
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''The wrapper method'''
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """This is a Cache using redis
    """

    def __init__(self) -> None:
        """Intialization for cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[bytes, str, float, int]) -> str:
        """A store method"""
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None
            ) -> Union[bytes, str, float, int, None]:
        """get original element"""
        val = self._redis.get(key)
        if fn:
            return fn(val)
        return val

    def get_str(self, data: str) -> str:
        """Decode the redis value"""
        return data.decode("utf-8")

    def get_int(self, data: str) -> int:
        """return the integer"""
        return int(data)
