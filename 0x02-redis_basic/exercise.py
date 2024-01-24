#!/usr/bin/env python3
""" exercise.py """
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count method calls"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ increments the count """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store input and output history of a function"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ reate input and output list keys """
        input_key = "{}:inputs".format(method.__qualname__)
        output_key = "{}:outputs".format(method.__qualname__)

        """ Append input arguments to the input list """
        self._redis.rpush(input_key, str(args))

        """ Execute the wrapped function to retrieve the output """
        result = method(self, *args, **kwargs)

        """ Store the output in the output list """
        self._redis.rpush(output_key, str(result))

        return result

    return wrapper


def replay(method: Callable) -> None:
    """
    Display the history of calls of a particular function.
    Retrieve input and output list keys
    """
    cache_instance = getattr(method.__self__, '_redis', None)

    input_key = "{}:inputs".format(method.__qualname__)
    output_key = "{}:outputs".format(method.__qualname__)

    """ Retrieve input and output lists from Redis """
    inputs = cache_instance.lrange(input_key, 0, -1)
    outputs = cache_instance.lrange(output_key, 0, -1)

    """ Display the history of calls """
    print(f"{method.__qualname__} was called {len(inputs)} times:")
    for input_args, output in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(
            method.__qualname__, input_args.decode("utf-8"), output))


class Cache:
    """ Create a Cache class """
    def __init__(self) -> None:
        """ Initialize Redis client and flush the database """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
