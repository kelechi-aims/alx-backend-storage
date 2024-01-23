#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


# Connect to MpngoDB
client = MongoClient('mongodb://127.0.0.1:27017')
db = client.logs
collection = db.nginx

if __name__ == "__main__":
    # Total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    print(f"Methods:")

    # Methods count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Number of logs wih method=GET and path=/status
    status_check_count = collection.count_documents(
            {"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")
