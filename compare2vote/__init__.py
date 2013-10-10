from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask("compare2vote")
mongo = PyMongo(app)

import compare2vote.views