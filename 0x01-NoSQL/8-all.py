#!/usr/bin/env python3
"""
List all documents in a collection
Prototype: def list_all(mongo_collection):
Return an empty list if no document in the collection
mongo_collection will be the pymongo collection object
"""


def list_all(mongo_collection):
    """
    Prototype: def list_all(mongo_collection)
    Return an empty list if no document in the collection
    """
    documents = mongo_collection.find()
    return documents
