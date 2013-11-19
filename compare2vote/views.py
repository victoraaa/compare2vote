from compare2vote import app
from flask import request, render_template

import bson.json_util as json_util
import flask, json, functools

import repository, poll_models, poll_service


def jsonify(decorated):
    @functools.wraps(decorated)
    def wrapper(*args, **kwargs):
        return flask.make_response(
            json.dumps(decorated(*args, **kwargs), default=json_util.default),
            200,
            {"Content-Type": "application/json"},
        )

    return wrapper


@app.route('/')
def home():
    polls = repository.get_all_polls()
    return render_template('rankings.html', polls=[_poll_viewmodel(poll) for poll in polls])


@app.route('/create')
def create():
    return render_template('new-poll.html')


@app.route('/create_poll', methods=["POST"])
def create_poll():
    data = json.loads(request.values.get("json"))
    poll = poll_service.create_poll_with_options(
        data["title"],
        data["question"],
        [
            poll_models.PollOption(option["name"], option["image_url"])
            for option in data["options"]
        ]
    )
    return flask.url_for('.edit_poll', poll_id=str(poll._id))


@app.route('/edit/<poll_id>', methods=["GET", "POST"])
def edit_poll(poll_id):
    poll = repository.get_poll_by_id(poll_id)
    return render_template('edit-poll.html', poll=_poll_viewmodel(poll))


@app.route('/add_option/<poll_id>', methods=["POST"])
def add_option(poll_id):
    new_option = json.loads(request.values.get("json"))["option"]
    poll_service.add_option_to_poll(
        poll_id, poll_models.PollOption(new_option["name"], new_option["image_url"])
    )
    return flask.url_for('.edit_poll', poll_id=str(poll_id))


@app.route('/voting_options/<poll_id>', methods=["GET"])
@jsonify
def voting_options(poll_id):
    options = poll_service.get_two_random_and_different_options(poll_id)
    return [_option_viewmodel(option) for option in options]


@app.route('/vote/<poll_id>', methods=["POST"])
def vote(poll_id):
    data = json.loads(request.values.get("json"))
    poll_service.compute_vote(poll_id, data["winner"], data["loser"])
    return "ok"

@app.route('/poll/<poll_id>', methods=["GET"])
def poll_options(poll_id):
    poll = repository.get_poll_by_id(poll_id)
    return render_template('poll.html', poll=_poll_viewmodel(poll))

def _poll_viewmodel(poll):
    return {
        "title": poll.title,
        "question": poll.question,
        "number_of_votes": len(poll.votes),
        "leaders": [_option_viewmodel(option) for option in poll.ranking[:3]],
        "options": [_option_viewmodel(option) for option in poll.ranking[:]],
        "votingOptionsUrl": flask.url_for('.voting_options', poll_id=str(poll._id)),
        "editUrl": flask.url_for('.edit_poll', poll_id=str(poll._id)),
        "voteUrl": flask.url_for('.vote', poll_id=str(poll._id)),
        "rankUrl": flask.url_for('.poll_options', poll_id=str(poll._id)),
        "_id": str(poll._id)
    }

def _option_viewmodel(option):
    return {
        "name": option.name,
        "image_url": option.image_url
    }