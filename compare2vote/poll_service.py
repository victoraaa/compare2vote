import random
import poll_models, repository


def create_poll_with_options(title, question, options):
	new_poll = poll_models.Poll(title, question)
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

