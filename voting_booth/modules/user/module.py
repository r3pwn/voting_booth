from flask import Blueprint, request
import os
import json
import uuid
import sqlite3
import hashlib
import binascii

CONFIG_FILE = 'voting_booth/modules/user/config.json'
user = Blueprint('user', __name__)

with open(CONFIG_FILE) as json_file:
    config = json.load(json_file)['config'][0]

@user.route('/login', methods = ['POST'])
def user_login():
    conn = sqlite3.connect(config['usersDb'])
    c = conn.cursor()

    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return "ERR", 400

    msg = "ERR"
    status = 403

    if does_user_exist(username):
        if verify_password(get_hashed_pw_for_user(username), password):
            msg = "OK, auth_code: " + get_auth_code_by_user(username)
            status = 200

    conn.commit()
    conn.close()

    return msg, status

@user.route('/register', methods = ['POST'])
def user_register():
    conn = sqlite3.connect(config['usersDb'])
    c = conn.cursor()

    username = request.form.get('username')
    password = request.form.get('password')
    affiliation = request.form.get('affiliation')

    if not username or not password or not affiliation:
        return "ERR", 400

    if not does_user_exist(username):
        try:
          sql = '''INSERT INTO users (username, password, affiliation, auth_code) VALUES (?, ?, ?, ?)'''
          c.execute(sql, (username, hash_password(password), affiliation, str(uuid.uuid4())))
        except:
          return "ERR", 500
    else:
        return "ERR", 409
    conn.commit()
    conn.close()

    return "OK", 200

def does_user_exist(username):
    conn = sqlite3.connect(config['usersDb'])
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=?", (username,))
 
    rows = c.fetchall()

    ret = False
    for row in rows:
        ret = True
    conn.commit()
    conn.close()
    return ret

def get_hashed_pw_for_user(username):
    conn = sqlite3.connect(config['usersDb'])
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=?", (username,))
 
    rows = c.fetchall()

    hash_pw = rows[0][2]

    conn.commit()
    conn.close()
    return hash_pw

def get_auth_code_by_user(username):
    conn = sqlite3.connect(config['usersDb'])
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=?", (username,))
 
    rows = c.fetchall()

    auth_code = rows[0][4]

    conn.commit()
    conn.close()
    return auth_code

def get_user_by_auth_code(auth_code):
    conn = sqlite3.connect(config['usersDb'])
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE auth_code=?", (auth_code,))
 
    rows = c.fetchall()

    user_acc = rows[0]

    conn.commit()
    conn.close()
    return user_acc

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
