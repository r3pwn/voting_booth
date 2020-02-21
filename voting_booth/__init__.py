from flask import Flask

app = Flask(__name__)

# load modules here
from voting_booth.main import main
from voting_booth.addons.user.module import user
from voting_booth.addons.vote.module import vote
from voting_booth.addons.results.module import results

# top-level API endpoints
app.register_blueprint(main, url_prefix='/')

# user authentication addon
app.register_blueprint(user, url_prefix='/user')

# perform the vote
app.register_blueprint(vote, url_prefix='/vote')

# show the results
app.register_blueprint(results, url_prefix='/results')
