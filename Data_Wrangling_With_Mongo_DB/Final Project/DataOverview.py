#!/usr/bin/env python
import pprint


def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    database = client[db_name]

    return database

if __name__ == '__main__':
    db = get_db('cities')

    # Number of documents
    print "Number of documents:", db.miami_fl.find().count()

    # Number of nodes
    print "Number of nodes:", db.miami_fl.find({"type": "node"}).count()

    # Number of ways
    print "Number of ways:", db.miami_fl.find({"type": "way"}).count()

    # Number of Royal Palm
    print "Number of Royal Palm:", db.miami_fl.find({"type": "Royal Palm"}).count()

    # Count all node types
    print "Count all node types:"
    pprint.pprint(db.miami_fl.aggregate([{
        "$group": {
            "_id": "$type",
            "count": {"$sum": 1}
        },
    }])['result'])

    # Number of unique users
    print "Number of unique users:", len(db.miami_fl.aggregate([{
        "$group": {"_id": "$created.user", "count": {"$sum": 1}}
    }])['result'])

    # Top 1 contributing user
    print "Top 1 contributing user:", db.miami_fl.aggregate([
        {"$group": {"_id": "$created.user", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 1}])['result']

    # Number of users appearing only once (having 1 post)
    print "Number of users appearing only once (having 1 post):", db.miami_fl.aggregate([
        {"$group": {"_id": "$created.user", "count": {"$sum": 1}}},
        {"$group": {"_id": "$count", "num_users": {"$sum": 1}}},
        {"$sort": {"_id": 1}},
        {"$limit": 1}])['result']

    # Earliest entry timestamp
    print "Earliest entry timestamp:", db.miami_fl.aggregate([{"$project": {"timestamp": "$created.timestamp"}},
                                {"$sort": {"timestamp": 1}},
                                {"$limit": 1}])['result']

    # Latest entry timestamp
    print "Latest entry timestamp:", db.miami_fl.aggregate([{"$project": {"timestamp": "$created.timestamp"}},
                                {"$sort": {"timestamp": -1}},
                                {"$limit": 1}])['result']

    # Count of entries by Year / Month, sorted by count
    print "Entries by Year / Month, sorted by Date:"
    pprint.pprint(db.miami_fl.aggregate([{"$project": {"datetime": {"$substr": ["$created.timestamp", 0, 7]}}},
                                              {"$group": {"_id": "$datetime", "count": {"$sum": 1}}},
                                              {"$sort": {"_id": -1}}]))

    # Analyze Postal Codes
    # print pprint.pprint(db.miami_flor.aggregate([
    #    {"$group": {"_id": "$address.postcode", "count": {"$sum": 1}}}])['result'])

    # Street types after cleaning
    print "Street types after cleaning:"
    pprint.pprint(db.miami_fl.aggregate([
        {"$group": {"_id": "$address.st_type", "count": {"$sum": 1}}}])['result'])
