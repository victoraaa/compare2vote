import collections
from bson.objectid import ObjectId

class VitinhoModel():

	def __init__(self):
		pass

	#This methods probably has many, many errors. I shall search the look for the way of doing this, but not now.
	def to_mongo_json(self):
		res = {}
		for key, value in self.__dict__.iteritems():
			if hasattr(value, "to_json"):
				res[key] = value.to_mongo_json()
			elif isinstance(value, list):
				res[key] = [
					val.to_mongo_json() if hasattr(val, "__dict__") else val
					for val in value
				]
			#elif isinstance(value, ObjectId):
			#	res[key] = str(value)
			else:
				res[key] = value
		return res



class PollOption(VitinhoModel):

	def __init__(self, name, image_url):
		VitinhoModel.__init__(self)
		self.name = name
		self.image_url = image_url


class _PollVote(VitinhoModel):

	def __init__(self, winner, loser):
		VitinhoModel.__init__(self)
		self.winner = winner
		self.loser = loser

class Poll(VitinhoModel):

	def __init__(self, title, question):
		VitinhoModel.__init__(self)
		self.title = title
		self.question = question
		self.options = []
		self.votes = []


	def add_option(self, option):
		if any(existing_option.name == option.name for existing_option in self.options):
			raise Exception("One may not add a option with the same name as an existing option.")
		self.options.append(option)


	def vote(self, winner, loser):
		self.votes.append(_PollVote(winner, loser))


	@property
	def ranking(self):
		def calculate_points(poll_option):
			return sum(vote.winner.name == poll_option.name for vote in self.votes)

		points = {
			poll_option.name: calculate_points(poll_option)
			for poll_option in self.options
		}

		ranking = sorted(self.options, lambda x, y: points[x.name] - points[y.name], reverse=True)
		return ranking

	@classmethod
	def from_json(cls, json):
		new_poll = Poll(json["title"], json["question"])
		for poll_option in json["options"]:
			new_poll.add_option(PollOption(poll_option["name"], poll_option["image_url"]))
		for vote in json["votes"]:
			new_poll.vote(vote)
		if "_id" in json:
			new_poll._id = json["_id"]
		return new_poll

















