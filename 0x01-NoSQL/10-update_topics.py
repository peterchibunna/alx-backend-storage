#!/usr/bin/env python3
"""
Module 10
"""


def update_topics(mongo_collection, name, topics):
    """change the topics of a school based on the name
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
