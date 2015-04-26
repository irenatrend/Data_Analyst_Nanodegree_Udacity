#!/usr/bin/env python

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    database = client[db_name]

    return database

if __name__ == '__main__':
    db = get_db('cities')

    # Delete database cities
    db.connection.drop_database('cities')
