import random
import poll_models, repository


def create_poll_with_options(title, question, options, password):
	new_poll = poll_models.Poll(title, question)
	new_poll.add_password(password)
	for choice in options:
		new_poll.add_option(choice)
	new_poll = repository.insert_poll(new_poll)
	return new_poll

def add_option_to_poll(poll_id, option):
	poll = repository.get_poll_by_id(poll_id)
	poll.add_option(option)
	repository.insert_poll(poll)

def get_two_random_and_different_options(poll_id):
	poll = repository.get_poll_by_id(poll_id)
	return random.sample(poll.options, 2)

def compute_vote(poll_id, winner_name, loser_name):
	poll = repository.get_poll_by_id(poll_id)
	poll.vote(poll.get_option_by_name(winner_name), poll.get_option_by_name(loser_name))
	repository.insert_poll(poll)