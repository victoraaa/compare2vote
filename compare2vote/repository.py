from compare2vote import mongo
from bson.objectid import ObjectId
import poll_models

import bson.json_util as json_util
import json

def get_all_polls():
	return [poll_models.Poll.from_json(poll) for poll in mongo.db.polls.find()]

def insert_poll(poll):
	poll._id = mongo.db.polls.save(poll.to_mongo_json())
	return poll

def get_poll_by_id(poll_id):
	return poll_models.Poll.from_json(mongo.db.polls.find_one({"_id": ObjectId(poll_id)}))