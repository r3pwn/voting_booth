from flask import Blueprint
import json

CONFIG_FILE = 'voting_booth/addons/user/config.json'
user = Blueprint('user', __name__)

with open(CONFIG_FILE) as json_file:
    config = json.load(json_file)['config'][0]

@user.route('/login')
def user_login():
    # TODO: implement hashing and verification here
    return "false", 403

@user.route('/getinfo')
def user_getinfo():
    # TODO: implement returning user info (if logged in) here
    return "false", 403
