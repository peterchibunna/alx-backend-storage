#!/usr/bin/env python3
"""
Module 11
"""
from pymongo import MongoClient


def get_collections():
    """returns the documents in the given collection"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    return logs


def main():
    """This is where all the work is done
    """
    logs = get_collections()
    print('{} logs'.format(logs.count_documents({})))
    print('Methods:')
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        log_count = list(logs.find({'method': method})).__len__()
        print('\tmethod {}: {}'.format(method, log_count))
    len_status = list(
        logs.find({'method': 'GET', 'path': '/status'})).__len__()
    print('{} status check'.format(len_status))


if __name__ == '__main__':
    main()
