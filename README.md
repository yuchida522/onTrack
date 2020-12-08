# OnTrack

OnTrack is a web app that lets users track their running progress

## Table of Contents

* [Tech Stack](#techstack)
* [Features](#features)
* [Setup](#setup)
* [About the Developer](#developer)

## <a name="techstack"></a>Tech Stack
__Front End:__ HTML, Jinja2, CSS, JavaScript, AJAX, Bootstrap, chart.js<br/>
__Back End:__ Python, Flask, PostgreSQL, SQLAlchemy

## <a name="features"></a>Features
GET STATS: Login to view your profile that gives key stats of your progress like number of runs, total distance, mileage, and pace.  

TRACK AND STORE RUNS: log your runs to keep track 

SET GOALS: Search and find a race to set goals for your training. Keep track of whether you've signed up.
## <a name="setup"></a>Setup
Requirements:
Python3, PostgreSQL
<br>
Clone repository:
```
$ git clone https://github.com/yuchida522/onTrack.git
```

Create a virtual environment:
```
$ virtualenv env
```

Activate the virtual environment:
```
$ source env/bin/activate
```

Install dependencies:
```
$ pip3 install -r requirements.txt
```

Make an account with [Active API](https://developer.active.com/docs/read/v2_Activity_API_Search) and get a free [API key](https://developer.active.com/member/register) <br>
Store the key in a file named 'secrets.sh':
![Secret](/static/ReadMe/secret_key.png)

Add the key to your environmental variables:
```
$ source secrets.sh
```

Create OnTrack database called 'races' with PostgreSQL:
```
$ createdb races
```

Seed database with data (optional - provided data is created by Faker, do this if you want to see what the rendered results will look like on each page) :
```
$ python3 seed_database.py
```

Run the app from the command line:
```
$ python3 server.py
```

Visit localhost:5000 on your browser. Enjoy!

## <a name="developer"></a>About the Developer

Yuri Uchida by training is a classical violinist, performing as an orchestral musican and maintaining a studio of 15 pre-college students. She first came across programming when she wanted to build her personal webiste and quickly realized her love for coding, as she found many similarities between coding and music. After a couple of months of self-learning, she decided to transition her career to software engineering and joined Hackbright Academy in September 2020. Post Hackbright, she looks forward to pursuing a full-time career as a software engineer and creating personal projects along the way.

Learn more about Yuri on her<a href="https://www.linkedin.com/in/yuri-uchida/">LinkedIn</a>