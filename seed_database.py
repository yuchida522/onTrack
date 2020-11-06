import os
import json
import requests

import crud
import model 

import server

from server import race_results


API_KEY = os.environ['API_KEY']

os.system('dropdb races')
os.system('createdb races')


#connect to database
model.connect_to_db(server.app)
model.db.create_all()

#import API
url = 'http://api.amp.active.com/v2/search?query=running'
payload = {'api_key': API_KEY}

response = requests.get(url, params=payload)

race_data = response.json() 

events = race_data['results']

for race in events:
	date = race['activityStartDate']
	city_name = race['place']['cityName']
	zipcode = race['place']['postalCode']
	race_url = race['homePageUrlAdr']
	race_description = race['assetDescriptions'][0].get('description')
	organization_name = race['organization']['organizationName']
	race_name = race['assetName']

	# city = crud.create_city(city_name, zipcode)

	# race = crud.create_race(race_name, date, city, url, race_description, organization_name)

# with open('/test_data/test_users.seed') as files:
	
# 	for line in files:
# 		user_info = line.split('|')
# 		print(user_info)


	










