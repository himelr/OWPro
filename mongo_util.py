# -*- coding: cp1252 -*-

import pymongo,datetime
from pymongo import MongoClient
from bson.json_util import loads,dumps


CLIENT_URL = 'ec2-54-194-96-92.eu-west-1.compute.amazonaws.com'
PORT = 27017
CLIENTM = MongoClient(CLIENT_URL,PORT)
DB = CLIENTM.owapi

def connect():
    print("Connecting")

    client = MongoClient('ec2-54-194-96-92.eu-west-1.compute.amazonaws.com', 27017)
    db = client.owapi
    collection = db.users
    post = {"author": "Mike",
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}

    #posts = db.movie
    post_id = collection.insert_one(post).inserted_id
    print(post_id)

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
        collection.update_one({'_id':fs["_id"]}, {"$set": fs}, upsert=False)

    else:
        document["updated"] = datetime.datetime.utcnow()
        data_id = collection.insert_one(document).inserted_id


def fetch_all_pros():
    collection = DB.leaderboards
    players = collection.find({})
    return dumps(players)

def find_one(user):

    stats = DB.game_stats
    fs = stats.find_one({"user.username": user})
    print(fs)
    if fs is None:
        return None
    else:
        return dumps(fs)

def add_player(user,name):
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








