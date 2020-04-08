from flask import Blueprint, request
import os
import json
import sqlite3

print("[WARN] @@@ LOADED UNSAFE USERS MODULE!!! @@@")

CONFIG_FILE = 'voting_booth/modules/user/config_insecure.json'
user = Blueprint('user', __name__)

with open(CONFIG_FILE) as json_file:
    config = json.load(json_file)['config'][0]

@user.route('/login', methods = ['POST'])
def user_login():
    print("[WARN] @@@ CALLED UNSAFE USERS MODULE ENDPOINT!!! @@@")
    conn = sqlite3.connect(config['usersDb'])
    c = conn.cursor()

    print(request.form)
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return "ERR", 400

    msg = "OK"
    status = 200

    if does_user_exist(username):
        print(get_user_password(username))
        if get_user_password(username) == password:
            msg = "OK"
            status = 200
        else:
            msg = "ERR"
            status = 403

    conn.commit()
    conn.close()

    return msg, status

@user.route('/register', methods = ['POST'])
def user_register():
    print("[WARN] @@@ CALLED UNSAFE USERS MODULE ENDPOINT!!! @@@")
    conn = sqlite3.connect(config['usersDb'])
    c = conn.cursor()

    print(request.form)
    username = request.form.get('username')
    password = request.form.get('password')
    affiliation = request.form.get('affiliation')

    if not username or not password or not affiliation:
        return "ERR", 400

    if not does_user_exist(username):
        #try:
          sql = ("INSERT INTO users (username, password, affiliation) VALUES (\""
                + username + "\",\"" + password + "\",\"" + affiliation + "\");")
          c.executescript(sql)
        #except:
        #  return "ERR", 500
    else:
        return "ERR", 409
    conn.commit()
    conn.close()

    return "OK", 200

def does_user_exist(username):
    conn = sqlite3.connect(config['usersDb'])
    c = conn.cursor()

    c.executescript("SELECT * FROM users WHERE username=\"" + username + "\";")
 
    rows = c.fetchall()

    ret = False
    for row in rows:
        ret = True
    conn.commit()
    conn.close()
    return ret

def get_user_password(username):
    conn = sqlite3.connect(config['usersDb'])
    c = conn.cursor()

    c.executescript("SELECT * FROM users WHERE username=\"" + username + "\";")
 
    rows = c.fetchall()

    password = rows[0][2]

    conn.commit()
    conn.close()
    return password

def get_user_by_username(username):
    conn = sqlite3.connect(config['usersDb'])
    c = conn.cursor()

    c.executescript("SELECT * FROM users WHERE username=\"" + username + "\";")
 
    rows = c.fetchall()

    user_acc = rows[0]

    conn.commit()
    conn.close()
    return user_acc
