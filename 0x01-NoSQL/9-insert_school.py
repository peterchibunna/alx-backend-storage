#!/usr/bin/env python3
"""
Module 9
"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on `kwargs`
    """
    document = mongo_collection.insert_one(kwargs)
    return document.inserted_id
