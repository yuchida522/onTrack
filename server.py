from flask import (Flask, render_template, request)
# flash, session, redirect)
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


@app.route('/search_races')
def search_races():
    
    return render_template('search_races.html')


@app.route('/race_results')
def race_results():

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

    return data
    events = data['results']
    
    return render_template('race_results.html',
                            data=data,
                            results=events)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

