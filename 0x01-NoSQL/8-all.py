#!/usr/bin/env python3
"""
Python function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    List all documents in the specified MongoDB collection.

    Args:
        mongo_collection: pymongo collection object.

    Returns:
        A list of documents in the collection.
    """
    return list(mongo_collection.find())
