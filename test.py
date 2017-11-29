# -*- coding: cp1252 -*-

import pymongo,datetime,pprint,scrapy,Brick
from pymongo import MongoClient
from Brick import BrickSetSpider

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


def findOne():

    client = MongoClient('ec2-54-194-96-92.eu-west-1.compute.amazonaws.com', 27017)
    db = client.owapi
    posts = db.users
    print(posts.find_one({"author": "Mike"}))


def main():
    print("hello")

    Spider = BrickSetSpider
    #connect()
    findOne()



if __name__ == "__main__":
    main()