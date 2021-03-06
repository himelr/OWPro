# -*- coding: cp1252 -*-

import pymongo, datetime
from pymongo import MongoClient
from bson.json_util import loads, dumps
from bson.objectid import ObjectId

CLIENT_URL = 'ec2-54-194-96-92.eu-west-1.compute.amazonaws.com'
PORT = 27017
CLIENTM = MongoClient(CLIENT_URL, PORT)
DB = CLIENTM.owapi


def save_stats(document):
    collection = DB.game_stats
    post_id = collection.insert_one(document).inserted_id
    print(post_id)


def save_score():
    collection = DB.leaderboard


def save_rank(document):
    collection = DB.leaderboards
    fs = collection.find_one({"user.username": document["user"]["username"]})

    if fs != None:
        fs["scores"] = document["scores"]
        fs["user"] = document["user"]
        fs['updated'] = datetime.datetime.utcnow()
        collection.update_one({'_id': fs["_id"]}, {"$set": fs}, upsert=False)

    else:
        document["updated"] = datetime.datetime.utcnow()
        data_id = collection.insert_one(document).inserted_id


def fetch_all_pros():
    collection = DB.leaderboards
    players = collection.find({})
    return dumps(players)


def fetch_heroboard():
    collection = DB.heroboards
    herodoc = collection.find_one({"_id": ObjectId("5a57e44a210e893130ef42db")})

    return dumps(herodoc)


def save_heroboard(doc):
    collection = DB.heroboards
    herodoc = collection.find_one({"_id": ObjectId("5a57e44a210e893130ef42db")})
    try:
        if herodoc == None:
            collection.insert(doc, check_keys=False)
        else:
            print("WWW")
            doc["_id"] = herodoc["_id"]
            collection.update({'_id': herodoc["_id"]}, {"$set": doc}, upsert=False, check_keys=False)

    except TypeError:
        return True


def find_one(user):
    stats = DB.game_stats
    fs = stats.find_one({"user.username": user})

    if fs is None:
        return None
    else:
        return dumps(fs)


def update_user(doc, username):
    stats = DB.game_stats
    fs = stats.find_one({"user.username": username})
    fs['updated'] = {"date": datetime.datetime.utcnow()}
    fs['competitive'] = doc['competitive']
    fs['quickplay'] = doc['quickplay']

    stats.update_one({'_id': fs["_id"]}, {"$set": fs}, upsert=False)

    return dumps(fs)


def add_player(user, name):
    users = DB.users
    fs = users.find_one({"username": user})

    if fs is None:
        return False


    else:

        try:
            fs['players'].append(name)

        except KeyError:
            fs['players'] = []
            fs['players'].append(name)

        users.update_one({'_id': fs["_id"]}, {"$set": fs}, upsert=False)
        return True


def find_profile(user):
    users = DB.users
    fs = users.find_one({"username": user})

    if fs is None:
        return None
    else:
        return dumps(fs)
