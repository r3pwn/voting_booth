from flask import Blueprint
import json

print("[WARN] @@@ LOADED UNSAFE VOTING MODULE!!! @@@")

CONFIG_FILE = 'voting_booth/modules/vote/config.json'
vote = Blueprint('vote', __name__)

with open(CONFIG_FILE) as json_file:
    config = json.load(json_file)['config'][0]

@vote.route('/submit')
def vote_submit():
    print("[WARN] @@@ CALLED UNSAFE VOTING MODULE ENDPOINT!!! @@@")
    # TODO: Implement vote submitting
    return "OK"
