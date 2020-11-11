from flask import (Flask, jsonify, render_template, request, flash, session, redirect)
import requests
import os
import crud
from datetime import datetime, date

# TODO:add classes from model.py
from model import connect_to_db
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'dev'

API_KEY = os.environ['API_KEY']
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():

    # if 'current_user' in session:
    #     return redirect('/profile')

    # else:
        return render_template('homepage.html')


########## USER AUTHENTICATION PROCESS ######################


@app.route('/', methods=['POST'])
def create_user():

    """handle creating new accounts"""

    #get all the input values from the 'create account' form
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    #search with the email provided to see if the user exists in db
    user = crud.get_user_by_email(email)

    #if the user does not exist, create user and add to db, redirect to homepage where the login is
    if user is None:
        user = crud.create_user(fname, lname, username, email, password)
        flash('Account created! Now log in.')
        return redirect('/')
        #if user already exists, flash message to say user already exists
    else:
        flash("User already exists. Please try again...")
        return redirect('/create-account')


@app.route('/profile', methods=['POST'])
def login():

    """handle login process"""

    #get all input values from login form
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)  
    
    if not user:
        flash('User does not exist. Create an account to sign in')
        return redirect('/')
    else:
        if not password:
            flash('Login unsuccessful. Try again')
            return redirect('/')
        else:
            session['current_user'] = user.user_id 
            flash('Login Successful!')
            current_user = session.get('current_user')
            
            races = crud.get_currentraces_by_id(current_user)

            return render_template('profile.html', current_user=user, current_races=races) 




@app.route('/logout', methods=['GET'])
def logout():
    
    session.pop('current_user', None)
    flash('Logged Out')
    return render_template('homepage.html')



@app.route('/create-account')
def show_create_user():

    return render_template('create-user.html')


########################## ENTRIES ##############################


@app.route('/training-log', methods=['POST'])
# @app.route('/training_log', methods=['GET', 'POST'])
def create_training_log():

    """creates new training entry to the training log"""

    # old_entries = crud.get_training_log_by_userid(current_user)
    current_user_id = session.get('current_user', None)
    
    if current_user_id:
        # if methods = POST
        # training_date = request.form.get('training_date')
        training_date = datetime.today()
        # print('\n\n\n\n\n\n\n\n\n\n\n\n')
        # print('type', type(training_date))
        # print(training_date)
        # print(datetime.fromisoformat(training_date))
        training_mileage = request.form.get('mileage_run')
        # print(training_mileage)
        training_effort = request.form.get('effort')
        # print(training_effort)
        training_comments = request.form.get('comments')
        # print(training_comments)
        crud.create_training_log(current_user_id, training_date, training_mileage, training_effort, training_comments)
        

        flash('New log created!')
        # return(new_entry)
        return redirect('/training-log')

        #if method is GET
            # current_user_logs = crud.get_training_log_by_userid(current_user)

            # return render_template('training_log.html', current_user_logs=current_user_logs)


@app.route('/training-log', methods=['GET'])
def show_training_logs():
    """shows the past training logs user has made"""

    #default to none if user does not exist
    current_user_id = session.get('current_user', None)

    if current_user_id:

        current_user_logs = crud.get_training_log_by_userid(current_user_id)

        return render_template('training-log.html', current_user_logs=current_user_logs)


@app.route('/search-races')
def search_races():
    
    return render_template('search-races.html')


@app.route('/race-results')
def race_results():

    #get the values from search_races form
    city_name = request.args.get('city_name', '')
    distance_length = request.args.get('distance_length', '')
    start_date = request.args.get('start_date', '')

    url = 'http://api.amp.active.com/v2/search?query=running&sort=date_asc'
    payload = {'api_key': API_KEY,
               'near': city_name,
               'query': distance_length,
               'start_date': start_date + '..'
               }
    
    response = requests.get(url, params=payload)
    data = response.json()

    
    events = data['results']
    
    #render results onto race_results page
    return render_template('race-results.html',
                            data=data,
                            results=events)

@app.route('/save-the-date', methods=['GET'])
def create_an_event():

    asset_guid = request.args.get('assetguid', '')

    url = 'http://api.amp.active.com/v2/search'

    payload = {'api_key': API_KEY,
               'asset.assetGuid': asset_guid
               }

    response = requests.get(url, params=payload)
    data = response.json()

    # race = data['results']

    return render_template('save-the-date.html',
                            data=data)
    
@app.route('/race-results', methods=['POST'])  
def save_the_date():
    # # savethe race
    # # save the race according to account
    # # redirect to search page    
    # save_race = CurrentRace(race=race, user_id=user_id, signup_status=signup_status)
    race_name = request.form.get('race_name')
    race_date = datetime.strptime(request.form.get('date'), '%Y-%m-%dT%H:%M:%S')
    race_city = request.form.get('city_name')
    race_zipcode = request.form.get('zipcode')
    race_url = request.form.get('race_url')
    race_description = request.form.get('race_description')
    race_organization_name = request.form.get('organization_name')
    signup_status = request.form.get('signup_status')
    print('\n\n\n\n\n\n\n\n\n\n\n\n')
    print(race_date)
    print(type(race_date))
    
    new_city = crud.create_city(race_city, race_zipcode)
    new_race = crud.create_race(race_name, race_date, new_city, race_url, race_description, race_organization_name)
    

    current_user_id = session.get('current_user', None)

    if current_user_id:

        crud.create_current_race(new_race, current_user_id, signup_status)
        
        flash('Race has been added!')
        return redirect('/race-results')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

