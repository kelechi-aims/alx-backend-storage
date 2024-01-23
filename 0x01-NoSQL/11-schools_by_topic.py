#!/usr/bin/env python3
"""
returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic

    Args:
        mongo_collection: the pymongo collection object
        topic  (string): topic searched
    """
    return list(mongo_collection.find({"topics": topic}))
