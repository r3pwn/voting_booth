from flask import Blueprint
import json

print("[WARN] @@@ LOADED UNSAFE RESULTS MODULE!!! @@@")

CONFIG_FILE = 'voting_booth/modules/results/config.json'
results = Blueprint('results', __name__)

with open(CONFIG_FILE) as json_file:
    config = json.load(json_file)['config'][0]

@results.route('/view')
def results_view():
    print("[WARN] @@@ CALLED UNSAFE RESULTS MODULE ENDPOINT!!! @@@")
    # TODO: implement viewing results here
    return "I win"
