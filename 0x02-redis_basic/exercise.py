#!/usr/bin/env python3
""" exercise.py """
import redis
import uuid
from typing import Union, Callable


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

    def get(
            self,
            key: str,
            fn: Callable = None
            ) -> Union[str, bytes, int, float]:
        """ Get data from Redis """
        data = self._redis.get(key)

        if data is None:
            return None

        """ Apply the conversion function if provided """
        return fn(data) if fn else data

    def get_str(self, key: str) -> Union[str, None]:
        """ Helper method for getting a string from cache """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """ Helper method for getting a integer from cache """
        return self.get(key, fn=int)
