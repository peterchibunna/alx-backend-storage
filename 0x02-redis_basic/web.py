#!/usr/bin/env python3
"""
5. Implementing an expiring web cache and tracker
"""
import functools
import redis
import requests
import typing


cache = redis.Redis()


def cache_the_page(method: typing.Callable) -> typing.Callable:
    """Module comment
    """
    @functools.wraps(method)
    def wrapper(url: str) -> str:
        """module comment
        """
        cache.incr('visited:{}'.format(url))
        content = cache.get('content:{}'.format(url))
        if content is not None:
            return content.decode('utf-8')
        content = method(url)
        cache.set('visited:{}'.format(url), 0)
        cache.setex('content:{}'.format(url), 10, content)
        return content
    return wrapper


@cache_the_page
def get_page(url: str) -> str:
    content = requests.get(url=url)
    return content.text