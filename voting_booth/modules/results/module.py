from flask import Blueprint
from json import JSONEncoder
import sqlite3
import json

CONFIG_FILE = 'voting_booth/modules/results/config.json'
results = Blueprint('results', __name__)

with open(CONFIG_FILE) as json_file:
    config = json.load(json_file)['config'][0]

class CandidateEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, Candidate):
            return object.__dict__
        else:
            # call base class implementation which takes care of
            # raising exceptions for unsupported types
            return json.JSONEncoder.default(self, object)

class Candidate:
  def __init__(self, name):
    self.name = name
    self.votes = 0

  def addVote(self):
    self.votes += 1

candidates = []

@results.route('/view')
def results_view():
    global candidates
    candidates = []

    conn = sqlite3.connect(config['resultsDb'])
    c = conn.cursor()

    c.execute("SELECT * FROM votes")
 
    rows = c.fetchall()

    # tally the votes
    for row in rows:
        candidate = row[2]
        get_candidate(candidate).addVote()
            
    conn.commit()
    conn.close()

    return json.dumps(candidates, cls=CandidateEncoder)

def get_candidate(name):
    global candidates
    for person in candidates:
        if person.name == name:
            return person
    newcomer = Candidate(name)
    candidates.append(newcomer)
    return newcomer

