import json
import urllib2
import pymongo

__author__ = 'SekthDroid'

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.reddit
stories = db.stories

stories.drop()

reddit = urllib2.urlopen("https://www.reddit.com/r/technology/.json")

parsed = json.loads(reddit.read())

[stories.insert_one(item["data"]) for item in parsed["data"]["children"]]