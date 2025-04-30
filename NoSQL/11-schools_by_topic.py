#!/usr/bin/env python3
"""
Module 11-schools_by_topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns list of schools with a specific topic

    Args:
        mongo_collection: pymongo collection object
        topic (str): topic to search for
    """
    return mongo_collection.find({"topics": topic})
