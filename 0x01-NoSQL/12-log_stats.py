#!/usr/bin/env python3
"""
Provide some stats about Nginx logs stored in MongoDB
Database: logs, Collection: nginx, Display same as example
first line: x logs, x number of documents in this collection
second line: Methods
5 lines with method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
one line with method=GET, path=/status
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    nginx_collection = client.logs.nginx
    number = nginx_collection.count()
    number_get = nginx_collection.find({"method": "GET"}).count()
    number_post = nginx_collection.find({"method": "POST"}).count()
    number_put = nginx_collection.find({"method": "PUT"}).count()
    number_patch = nginx_collection.find({"method": "PATCH"}).count()
    number_delete = nginx_collection.find({"method": "DELETE"}).count()
    number_status = nginx_collection.find(
        {"method": "GET", "path": "/status"}).count()

    print("{} logs".format(number))
    print("Methods:")
    print("\tmethod GET: {}".format(number_get))
    print("\tmethod POST: {}".format(number_post))
    print("\tmethod PUT: {}".format(number_put))
    print("\tmethod PATCH: {}".format(number_patch))
    print("\tmethod DELETE: {}".format(number_delete))
    print("{} status check".format(number_status))
