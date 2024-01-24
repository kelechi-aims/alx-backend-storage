#!/usr/bin/env python3
""" wep.py """
import requests
import redis
from functools import wraps
from typing import Callable


def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of times a function is called"""
    @wraps(method)
    def wrapper(url: str) -> str:
        """ Initialize Redis client """
        redis_store = redis.Redis()

        """ Increment access count for the URL """
        url_key = f"count:{url}"
        access_count = redis_store.incr(url_key)

        """ Cache the result with an expiration time of 10 sec """
        result_key = f"result:{url}"
        cached_result = redis_store.get(result_key)

        if cached_result:
            return cached_result.decode("utf-8")

        """ Call the original function """
        result = method(url)

        """ Cache the result with expiration """
        redis_store.setex(result_key, 10, result)

        return result

    return wrapper


@count_calls
def get_page(url: str) -> str:
    """ Function to obtain HTML content or a URL """
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    # Example usage
    slow_url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.google.com"
    content = get_page(slow_url)
    print(content)
