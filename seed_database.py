import os
import json
import requests

import crud
import model 

import server

from random import choice


API_KEY = os.environ['API_KEY']

os.system('dropdb races')
os.system('createdb races')


#connect to database
model.connect_to_db(server.app)
model.db.create_all()


#create users

users_in_db = []

with open('test_data/test_users.txt') as f:

	for line in f:
		user_info = line.split('|')

		fname = user_info[0]
		lname = user_info[1]
		username = user_info[2]
		email = user_info[3]
		password = user_info[4]

		user = crud.create_user(fname, lname, username, email, password)

		users_in_db.append(user)

#import API
url = 'http://api.amp.active.com/v2/search?query=running'
payload = {'api_key': API_KEY,
               'near': 'San Francisco',
               'query': '5k',
               'start_date': '2021-1-1..'
               }

response = requests.get(url, params=payload)

race_data = response.json() 

events = race_data['results']

races_in_db = []

for race in events:
	date = race['activityStartDate']
	city_name = race['place']['cityName']
	zipcode = race['place']['postalCode']
	race_url = race['homePageUrlAdr']
	race_description = race['assetDescriptions'][0].get('description')
	organization_name = race['organization']['organizationName']
	race_name = race['assetName']

	city = crud.create_city(city_name, zipcode)

	race = crud.create_race(race_name, date, race_url, race_description, organization_name)

	races_in_db.append(race)

for user in users_in_db:

	race_random = choice(races_in_db)

	current_race = crud.create_current_race(race_random, user, signup_status=True)

	




	










