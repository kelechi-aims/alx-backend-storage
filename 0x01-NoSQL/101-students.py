#!/usr/bin/env python3
"""
Python function that returns all students sorted by average score
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score

    Args:
        mongo_collection: the pymongo collection object
    """
    pipeline = [
        {
            "$project": {
                "id": 1,
                "name":  1,
                "averageScore": {
                    "$avg": "$topics.score"
                 },
            }
        },
        {
           "$sort": {"averageScore": -1}
        }
    ]
    average = list(mongo_collection.aggregate(pipeline))
    return average
