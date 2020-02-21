import json
from flask import Blueprint

main = Blueprint('main', __name__)

@main.route("/version")
def appinfo():
    with open('appinfo.json') as json_file:
        data = json.load(json_file)
        for p in data['appinfo']:
            return p['version']

