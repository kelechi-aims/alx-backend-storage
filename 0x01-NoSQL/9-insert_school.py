#!/usr/bin/env python3
"""
Inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in a collection based on keyword arguments.

    Args:
        mongo_collection: pymongo collection object.
        **kwargs: Keyword arguments representing the fields
        and values of the new document.

    Returns:
        str: The _id of the newly inserted document.
    """
    document = mongo_collection.insert_one(kwargs)
    return document.inserted_id
