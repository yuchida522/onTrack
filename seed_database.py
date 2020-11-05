import os
import json
import requests

import crud
import model
import server

os.system('dropdb races')
os.system('createdb races')


#connect to database
model.connect_to_db(server.app)
model.db.create_all()

url = "http://api.amp.active.com/v2/search?sort=date_asc&api_key=dfquqhqma2ybzxe9p8usc4ys&start_date=2021-01-01..2021-09-26&query=half%20marathon&category=event&radius=500&near=San%20Francisco,CA,US&per_page=1000"

payload = {}
headers = {
  'Cookie': 'TS01a59dd9=01572f3dbe4adb0e784043aa112651bd049edc0f0527e2eaab974b4e4024d57395ab0d1b5c1bfcedc4a29c97fd16813f89cb9df8b8'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
races_in_db = []


