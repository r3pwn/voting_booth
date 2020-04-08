from flask import Flask
import json

app = Flask(__name__)

# load modules here
from voting_booth.main import main

# load proper modules based on the security setting
with open('appinfo.json') as json_file:
  data = json.load(json_file)
  for p in data['appinfo']:
    if p['security'] == "insecure":
      from voting_booth.modules.user.unsafe import user
      from voting_booth.modules.vote.unsafe import vote
      from voting_booth.modules.results.unsafe import results
    else:
      from voting_booth.modules.user.module import user
      from voting_booth.modules.vote.module import vote
      from voting_booth.modules.results.module import results

# top-level API endpoints
app.register_blueprint(main, url_prefix='/')

# user authentication addon
app.register_blueprint(user, url_prefix='/user')

# perform the vote
app.register_blueprint(vote, url_prefix='/vote')

# show the results
app.register_blueprint(results, url_prefix='/results')
