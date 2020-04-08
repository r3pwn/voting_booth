from flask import Blueprint, request
import voting_booth.modules.user as user
import sqlite3
import json

CONFIG_FILE = 'voting_booth/modules/vote/config.json'
vote = Blueprint('vote', __name__)

with open(CONFIG_FILE) as json_file:
    config = json.load(json_file)['config'][0]

@vote.route('/submit', methods = ['POST'])
def vote_submit():
    auth_code = request.form.get('auth_code')
    candidate = request.form.get('candidate')

    if not auth_code or not candidate:
        return "ERR", 400

    msg = "ERR"
    status = 403
    try:
      voter = user.module.get_user_by_auth_code(auth_code)
    except:
      return msg, status

    if (already_voted(voter)):
        msg = config['alreadyVotedMessage']
        status = 409
    else:
        count_vote(voter, candidate)
        msg = "OK"
        status = 200
    return msg, status

def count_vote(voter, candidate):
    conn = sqlite3.connect(config['resultsDb'])
    c = conn.cursor()

    try:
      sql = '''INSERT INTO votes (voter_id, candidate, affiliation) VALUES (?, ?, ?)'''
      c.execute(sql, (voter[0], candidate, voter[3]))
    except:
      return "ERR", 500
 
    conn.commit()
    conn.close()

def already_voted(voter):
    conn = sqlite3.connect(config['resultsDb'])
    c = conn.cursor()

    c.execute("SELECT * FROM votes WHERE voter_id=?", (voter[0],))
 
    rows = c.fetchall()

    ret = False
    for row in rows:
        ret = True
    conn.commit()
    conn.close()
    return ret
