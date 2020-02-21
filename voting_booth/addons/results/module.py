from flask import Blueprint
import json

CONFIG_FILE = 'voting_booth/addons/results/config.json'
results = Blueprint('results', __name__)

with open(CONFIG_FILE) as json_file:
    config = json.load(json_file)['config'][0]

@results.route('/view')
def results_view():
    # TODO: implement viewing results here
    return "I win"
