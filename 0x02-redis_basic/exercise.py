#!/usr/bin/env python3
""" exercise.py """
import redis
import uuid
from typing import Union


class Cache:
    """ Create a Cache class """
    def __init__(self) -> None:
        """ Initialize Redis client and flush the database """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generate a random key using uuid """
        key = str(uuid.uuid4())
        """ Store data in Redis using the generated key """
        self._redis.set(key, data)
        return key
