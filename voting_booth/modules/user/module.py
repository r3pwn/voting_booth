from flask import Blueprint, request
import os
import json
import sqlite3

CONFIG_FILE = 'voting_booth/modules/user/config.json'
user = Blueprint('user', __name__)

with open(CONFIG_FILE) as json_file:
    config = json.load(json_file)['config'][0]

conn = sqlite3.connect(config['usersDb'])
c = conn.cursor()

@user.route('/login')
def user_login():
    # TODO: implement hashing and verification here
    return "false", 403

@user.route('/getinfo')
def user_getinfo():
    # TODO: implement returning user info (if logged in) here
    return "false", 403

@user.route('/register', methods = ['POST'])
def user_register():
    username = request.form.get('username')
    password = request.form.get('password')
    affiliation = request.form.get('affiliation')

    try:
      sql = '''INSERT INTO users (username, password, affiliation) VALUES (?, ?, ?)'''
      c.execute(sql, companies)
    except sqlite3.IntegrityError as e:
      print('sqlite error: ', e.args[0]) # column name is not unique
    conn.commit()
    conn.close()

    print('done')
    for user in devices:
        if dev.udid == udid:
            # dev.values[value] = 
            return "OK", 200
        # device not found
        return "ERR", 404
    return "false", 403

def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password
