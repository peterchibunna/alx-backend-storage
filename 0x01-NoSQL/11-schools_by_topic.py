#!/usr/bin/env python3
"""
Module 11
"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic
    """
    results = mongo_collection.find({'topics': {'$elemMatch': {'$eq': topic}}})
    return [document for document in results]
