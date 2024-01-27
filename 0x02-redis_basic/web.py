#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""
import redis
from typing import Callable
from functools import wraps
import requests


def tracker(fn: Callable) -> Callable:
    """
    a decorator that takes a function Callable argument and returns a
    Callable
    """
    @wraps(fn)
    def wrapper(arg: str) -> str:
        """
        a wrapper function that track for that url how many times a
        particular URL was accessed
        """
        r = redis.Redis()
        r.incr("count:{{{}}}".format(arg))

        r.set(arg, 10, 10)
        HTML = fn(arg)
        r.set(arg, HTML, 10)
        return HTML
    return wrapper


@tracker
def get_page(url: str) -> str:
    """obtain the HTML content of a particular URL and returns it."""
    r = requests.get(url)
    return r.text