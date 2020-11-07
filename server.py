from flask import (Flask, render_template, request, flash, session, redirect)
import requests
import os

from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'API_KEY'

API_KEY = os.environ['API_KEY']
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():

    return render_template('homepage.html')


@app.route('/hello', methods=['POST'])
def login():
    # TODO: Need to implement this!

    # The logic here should be something like:
    #
    # - get user-provided name and password from request.form
    # - use customers.get_by_email() to retrieve corresponding Customer
    #   object (if any)
    # - if a Customer with that email was found, check the provided password
    #   against the stored one
    # - if they match, store the user's email in the session, flash a success
    #   message and redirect the user to the "/melons" route
    # - if they don't, flash a failure message and redirect back to "/login"
    # - do the same if a Customer with that email doesn't exist
    
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user is None:
        flash('Login unsuccessful. Try again')
        return redirect('/')
    else:
        flash('Login Successful!')
        return redirect('/hello')

        


@app.route('/create_account')
def show_create_user():

    return render_template('create_user.html')


@app.route('/', methods=['POST'])
def create_user():

    fname = request.form.get('fname')
    lname = request.form.get('lname')
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user is None:
        user = crud.create_user(fname, lname, username, email, password)
        flash('Account created! Now log in.')
        return redirect('/')
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

