#!/usr/bin/env python3
import sqlite3
import json

USER_CONFIG_FILE = 'voting_booth/modules/user/config.json'
with open(USER_CONFIG_FILE) as json_file:
    user_config = json.load(json_file)['config'][0]

RESULTS_CONFIG_FILE = 'voting_booth/modules/results/config.json'
with open(RESULTS_CONFIG_FILE) as json_file:
    results_config = json.load(json_file)['config'][0]

# set up an empty "users" database
def setup_users_db():
    conn = sqlite3.connect(user_config['usersDb'])
    c = conn.cursor()

    # Create table - USERS
    c.execute('''CREATE TABLE USERS
             ([id] INTEGER PRIMARY KEY, [username] text, [password] text, [affiliation] text, [auth_code] text)''')

    print("Users database created!")

    conn.commit()

# set up an empty "votes" database
def setup_results_db():
    conn = sqlite3.connect(results_config['resultsDb'])
    c = conn.cursor()

    # Create table - VOTES
    c.execute('''CREATE TABLE VOTES
             ([vote_id] INTEGER PRIMARY KEY, [voter_id] integer, [candidate] text, [affiliation] text)''')

    print("Results database created!")

    conn.commit()

if __name__ == '__main__':
    setup_users_db()
    setup_results_db()
