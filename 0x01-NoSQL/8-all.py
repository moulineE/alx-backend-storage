#!/usr/bin/env python3
"""function that lists all documents in a collection"""


def list_all(mongo_collection):
    """
    lists all documents in mongodb a collection

    :param mongo_collection:
    :return a mongodb command to find all document in a collection:
    """
    return mongo_collection.find()
