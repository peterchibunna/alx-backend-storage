#!/usr/bin/env python3
"""
Module 8
"""


def list_all(mongo_collection):
    """list all documents in the given collection
    """
    return [document for document in mongo_collection.find()]
