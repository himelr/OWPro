# -*- coding: cp1252 -*-

import pymongo,datetime
from pymongo import MongoClient
from bson.json_util import loads,dumps
from Brick import BrickSetSpider

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

def find_one(user):

    stats = DB.game_stats
    fs = stats.find_one({"user.username": user})
    print(fs)

    return dumps(fs)




