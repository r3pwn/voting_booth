from flask import Blueprint
import json

CONFIG_FILE = 'voting_booth/addons/vote/config.json'
vote = Blueprint('vote', __name__)

with open(CONFIG_FILE) as json_file:
    config = json.load(json_file)['config'][0]

@vote.route('/submit')
def vote_submit():
    # TODO: Implement vote submitting
    return "OK"
