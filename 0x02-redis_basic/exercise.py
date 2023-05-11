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
