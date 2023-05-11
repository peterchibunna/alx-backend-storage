#!/usr/bin/env python3
"""
0x02. Redis basic
- Learn how to use redis for basic operations
- Learn how to use redis as a simple cache
"""
import functools
import redis
import typing
import uuid


def count_calls(method: typing.Callable) -> typing.Callable:
    """In this task, we will implement a system to count how many times methods
    of the Cache class are called.
    Above Cache define a count_calls decorator that takes a single method
    Callable argument and returns a Callable.

    As a key, use the qualified name of method using the __qualname__ dunder
    method.

    Create and return function that increments the count for that key every
    time the method is called and returns the value returned by the original
    method."""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs) -> typing.Any:
        """implement a system to count how many times
        methods of the Cache class are called.
        """
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    def __init__(self) -> None:
        """initialise the redis cache
        """
        self._redis = redis.Redis()
        self._redis.flushdb(asynchronous=True)

    @count_calls
    def store(self, data: typing.Union[str, bytes, int, float]) -> str:
        """0. Writing strings to Redis
        """
        key = uuid.uuid5(uuid.NAMESPACE_X500, 'redis_test').__str__()
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: typing.Callable = None) \
            -> typing.Union[str, bytes, int, float]:
        """1. Reading from Redis and recovering original type
        """
        data = self._redis.get(key)
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """force the get to be a `string`"""
        return self.get(key).__str__()

    def get_int(self, key: str) -> int:
        """force the get to return an `int`"""
        return int(self.get(key))
