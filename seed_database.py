import os
import json
import requests

import crud
import model
# from model import db, User, Race, City, CurrentRace, TrainingLog
import server

from random import choice


API_KEY = os.environ['API_KEY']

os.system('dropdb races')
os.system('createdb races')


#connect to database
model.connect_to_db(server.app)
model.db.create_all()


#create users

#have a list of users, use later to create current_races table
users_in_db = []

#open the test_users file to create users in db
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


f = open('test_data/test_training_log.txt')

for line in f:
	training_info = line.split('|')
	training_date = training_info[0]
	training_mileage = training_info[1]
	training_effort = training_info[2]
	training_comment = training_info[3]
	training_run_time = training_info[4]

	for user in users_in_db:
		print('\n\n\n\n\n\n')
		print('*********////////////')
		print('IS THIS USER????', user)
		print('*********')
		training_log = crud.create_training_log(user.user_id, training_date, training_mileage, training_effort, training_comment, training_run_time)
		print('\n\n\n\n\n\n')
		print('*********')
		print(training_log)

		
#import API, for test purposes param is set to search races in SF beyond Jan 1, 2021
url = 'http://api.amp.active.com/v2/search?query=running'
payload = {'api_key': API_KEY,
               'near': 'San Francisco',
               'query': '5k',
               'start_date': '2021-1-1..'
               }

response = requests.get(url, params=payload)

race_data = response.json() 

#where the list of races exist
events = race_data['results']

#save each race to a list to again for later when creating current_races table
races_in_db = []

for race in events:
	date = race['activityStartDate']
	city_name = race['place']['cityName']
	zipcode = race['place']['postalCode']
	race_url = race['homePageUrlAdr']
	race_description = race['assetDescriptions'][0].get('description')
	organization_name = race['organization']['organizationName']
	race_name = race['assetName']

	#seeding data into cities table
	city = crud.create_city(city_name, zipcode)

	#seeding data into races table
	race = crud.create_race(race_name, date, city, race_url, race_description, organization_name)

	races_in_db.append(race)

for user in users_in_db:

	# #choose a race for each user from the list of races saved in races_in_db
	race = choice(races_in_db)
	#seeding data into current races table
	current_race = crud.create_current_race(race, user.user_id, signup_status="Yes", completed_status="Yes", comments="First race of the year!")
	


	




	










