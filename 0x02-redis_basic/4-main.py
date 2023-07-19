#!/usr/bin/python3
Cache = __import__('exercise').Cache
replay = __import__('exercise').replay

cache = Cache()

cache = Cache()
cache.store("foo")
cache.store("bar")
cache.store(42)
replay(cache.store)
