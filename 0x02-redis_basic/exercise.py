#!/usr/bin/env python3
"""the Redis basic exercise module"""
import redis
from typing import Union
import uuid


class Cache:
    """cache class that init an instalce of redice and flush it"""
    def __init__(self) -> None:
        """init and flush new Calche object"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store the input data in Redis using the random key and return the key
        :param data:
        :return key:
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
