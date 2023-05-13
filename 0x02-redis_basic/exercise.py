#!/usr/bin/env python3
"""
0x02. Redis basic
- Learn how to use redis for basic operations
- Learn how to use redis as a simple cache
"""
import functools
import random
import redis
import string
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


def call_history(method: typing.Callable) -> typing.Callable:
    """decorator to store the history of inputs and outputs for a
        particular function.
        Everytime the original function will be called, we will add its input
        parameters to one list in redis, and store its output into another
        list.
        In call_history, use the decorated function’s qualified name and
        append ":inputs" and ":outputs" to create input and output list keys,
        respectively"""

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs) -> typing.Any:
        """decorator to store the history of inputs and outputs for a
        particular function.
        Everytime the original function will be called, we will add its input
        parameters to one list in redis, and store its output into another
        list.
        In call_history, use the decorated function’s qualified name and
        append ":inputs" and ":outputs" to create input and output list keys,
        respectively
        """
        key_input = '{}:inputs'.format(method.__qualname__)
        key_output = '{}:outputs'.format(method.__qualname__)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(key_input, str(args))

        execution = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(key_output, execution)
        return execution

    return wrapper


def replay(fn: typing.Callable) -> typing.Any:
    """implement a replay function to display the history of calls of a
    particular function.
    """
    if fn is not None and hasattr(fn, '__self__'):
        store = fn.__self__._redis
        if isinstance(store, redis.Redis):
            method = fn.__qualname__
            inputs = store.lrange("{}:inputs".format(method), 0, -1)
            outputs = store.lrange("{}:outputs".format(method), 0, -1)
            try:
                print('{} was called {} times:'.format(method, len(inputs)))
                for _input, output in zip(inputs, outputs):
                    print('{}(*{}) -> {}'.format(method, _input.decode(
                        'utf-8'), output))
            except Exception:
                pass
    return


class Cache:
    """The cache class
    """

    def __init__(self) -> None:
        """initialise the redis cache
        """
        self._redis = redis.Redis()
        self._redis.flushdb(asynchronous=True)

    @call_history
    @count_calls
    def store(self, data: typing.Union[str, bytes, int, float]) -> str:
        """0. Writing strings to Redis
        """
        n = ''.join(
            random.choices(string.ascii_lowercase + string.hexdigits, k=10))
        key = uuid.uuid5(uuid.NAMESPACE_X500, '{}'.format(n)).__str__()
        # fixed: key wasn't changing after instantiation
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
