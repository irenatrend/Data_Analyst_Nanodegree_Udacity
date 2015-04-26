#!/usr/bin/env python
import pprint


def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    database = client[db_name]

    return database

if __name__ == '__main__':
    db = get_db('cities')

    # Count different Amenities
    print "Count different Amenities:"
    pprint.pprint(db.miami_fl.aggregate(([
        {"$group": {"_id": "$amenity",  "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}]))['result'])

    # Top 10 appearing amenities
    print "Top 10 appearing amenities:"
    pprint.pprint(db.miami_fl.aggregate([{"$match": {"amenity": {"$exists": 1}}},
                                              {"$group": {"_id": "$amenity", "count": {"$sum": 1}}},
                                              {"$sort": {"count": -1}},
                                              {"$limit": 10}])['result'])

    # Number of cafes
    print "Number of cafes:", db.miami_fl.find({"amenity": "cafe"}).count()

    # Number of Dunkin Donuts
    print "Number of Dunkin Donuts:", db.miami_fl.find({"name": "Dunkin Donuts"}).count()

    # Number of shops
    print "Number of shops:", db.miami_fl.find({"shop": {"$exists": "true"}}).count()

    # Restaurant's name, the food they serve, contact number and opening hours
    print "Restaurants:"
    pprint.pprint(db.miami_fl.aggregate([
        {'$match': {'amenity': 'restaurant', 'name': {'$exists': 1}}},
        {'$project': {'_id': '$name', 'cuisine': '$cuisine', 'contact': '$phone', 'opening_hours': '$opening_hours'}}])
    ['result'])

    # Nightclubs, phone contact and opening hours
    print "Nightclubs:"
    pprint.pprint(db.miami_fl.aggregate([
        {'$match': {'amenity': 'nightclub', 'name': {'$exists': 1}}},
        {'$project': {'_id': '$name', 'contact': '$phone', 'opening_hours': '$opening_hours'}}])['result'])

    # Biggest religion (no surprise here)
    print "Biggest religion:"
    pprint.pprint(db.miami_fl.aggregate([
                                {"$match": {"amenity": {"$exists": 1}, "amenity": "place_of_worship"}},
                                {"$group": {"_id": "$religion", "count": {"$sum": 1}}},
                                {"$sort": {"count": -1}},
                                {"$limit": 1}])['result'])

    # Most popular cuisines
    print "Top 5 most popular cuisines:"
    pprint.pprint(db.miami_fl.aggregate([
                                {"$match": {"amenity": {"$exists": 1}, "amenity": "restaurant"}},
                                {"$group": {"_id": "$cuisine", "count": {"$sum": 1}}},
                                {"$sort": {"count": -1}},
                                {"$limit": 5}])['result'])