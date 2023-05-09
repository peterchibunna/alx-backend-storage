#!/usr/bin/env python3
"""
Module 11
"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic
    """
    return [
        document for document in
        mongo_collection.find({"topic": {"$elemMatch": {"$eq": topic}}})
    ]
