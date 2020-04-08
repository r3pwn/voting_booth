#!/usr/bin/env python3
from voting_booth import app
import json

if __name__ == '__main__':
  # load proper modules based on the security setting
  with open('appinfo.json') as json_file:
    data = json.load(json_file)
    for p in data['appinfo']:
      app.run(port=p['portNum'])
