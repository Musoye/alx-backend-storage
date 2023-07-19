#!/usr/bin/python3
Cache = __import__('exercise').Cache

cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    print(cache.get_str(cache.get(key)))
    assert cache.get(key, fn=fn) == value
