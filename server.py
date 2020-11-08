from flask import (Flask, render_template, request, flash, session, redirect)
import requests
import os
import crud
 

from model import connect_to_db
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'dev'

API_KEY = os.environ['API_KEY']
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():

    return render_template('homepage.html')


@app.route('/hello', methods=['POST'])
def login():
    
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    
    if user is None:
        flash('User does not exist. Create an account to sign in')
        return redirect('/')
    else:
        if password is None:
            flash('Login unsuccessful. Try again')
            return redirect('/')
        else:
            session['logged_in'] = True
            flash('Login Successful!')
            return render_template('hello.html', user=user)
            


@app.route('/create_account')
def show_create_user():

    return render_template('create_user.html')


@app.route('/', methods=['POST'])
def create_user():

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
        return redirect('/create_account')


@app.route('/hello')
def hello():


    return render_template('hello.html')


@app.route('/search_races')
def search_races():
    
    return render_template('search_races.html')


@app.route('/race_results')
def race_results():

    #get the values from search_races form
    city_name = request.args.get('city_name', '')
    distance_length = request.args.get('distance_length', '')
    start_date = request.args.get('start_date', '')

    url = 'http://api.amp.active.com/v2/search?query=running'
    payload = {'api_key': API_KEY,
               'near': city_name,
               'query': distance_length,
               'start_date': start_date + '..'
               }
    
    response = requests.get(url, params=payload)
    data = response.json()

    
    events = data['results']
    
    #render results onto race_results page
    return render_template('race_results.html',
                            data=data,
                            results=events)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

