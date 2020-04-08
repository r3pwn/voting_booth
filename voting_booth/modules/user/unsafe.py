from flask import Blueprint, request
import json
import csv
import hashlib

print("[WARN] @@@ LOADED UNSAFE USER MODULE!!! @@@")

CONFIG_FILE = 'voting_booth/modules/user/config.json'
user = Blueprint('user', __name__)

with open(CONFIG_FILE) as json_file:
    config = json.load(json_file)['config'][0]

USERS_DB = 'ucuapi/addons/service/' + config['usersDb']

with open(CONFIG_FILE) as json_file:
    config = json.load(json_file)['config'][0]

@user.route('/login')
def user_login():
    print("[WARN] @@@ CALLED UNSAFE USER MODULE ENDPOINT!!! @@@")
    # TODO: implement hashing and verification here
    return "false", 403

@user.route('/getinfo')
def user_getinfo():
    print("[WARN] @@@ CALLED UNSAFE USER MODULE ENDPOINT!!! @@@")
    # TODO: implement returning user info (if logged in) here
    return "false", 403
