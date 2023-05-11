#!/usr/bin/env python3
"""
0x02. Redis basic
- Learn how to use redis for basic operations
- Learn how to use redis as a simple cache
"""
import redis
import typing
import uuid


class Cache:
    def __init__(self) -> None:
        """initialise the redis cache
        """
        self._redis = redis.Redis()
        self._redis.flushdb(asynchronous=True)

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
