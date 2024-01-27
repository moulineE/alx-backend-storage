#!/usr/bin/env python3
"""the Redis basic exercise module"""
import redis
from typing import Union, Optional, Callable, Any
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    decorator that takes a single method Callable argument and returns a
    Callable
    :param method:
    :return:
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> str:
        """
        a wrapper function that count for that key every time the method
        is called and returns the value returned by the original method
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """cache class that init an instalce of redice and flush it"""
    def __init__(self) -> None:
        """init and flush new Calche object"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store the input data in Redis using the random key and return the key
        :param data:
        :return key:
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """
        method that take a key string argument and
        an optional Callable argument named fn.
        This callable will be used to convert the data
        back to the desired format.
        Args:
            key(str): a key to the redis database data
            fn(Callable): optional callable to convert the data
        """
        data = self._redis.get(key)
        if data is None:
            return
        if fn is str:
            self.get_str(data)
        if fn is int:
            self.get_int(data)
        if callable(fn):
            return fn(data)
        return data

    def get_str(self, data: Any) -> str:
        """convert data to string type"""
        return data.decode("utf-8")

    def get_int(self, data: Any) -> int:
        """convert data to int type"""
        return int(data)
