# OnTrack

OnTrack is a web app that lets users track their running progress and set goals by searching and saving races they wish to participate

## Table of Contents

* [Tech Stack](#techstack)
* [Features](#features)
* [Setup](#setup)
* [About the Developer](#developer)

## <a name="techstack"></a>Tech Stack
__Front End:__ HTML, Jinja2, CSS, JavaScript, AJAX, Bootstrap, chart.js<br/>
__Back End:__ Python, Flask, PostgreSQL, SQLAlchemy

## <a name="features"></a>Features
GET STATS: Login to view your profile that gives key stats of your progress like number of runs, total distance, mileage, and pace <br/>
![stats](/static/ReadMe/stats.gif)
<br/>
<br/>
TRACK AND STORE RUNS: log your runs to keep track <br/>
![track](/static/ReadMe/log.gif)
<br/>
<br/>
SET GOALS: Search and find a race to set goals for your training. Keep track of whether you've signed up <br/>
![goals](/static/ReadMe/goals.gif)
<br/>
<br/>
## <a name="setup"></a>Setup
Requirements:
Python3, PostgreSQL
<br/>
1. Clone repository:
```
$ git clone https://github.com/yuchida522/onTrack.git
```
2. Install virtualenv:
```
pip install virtualenv
```

3. cd to /onTrack and run the following command to create a virtual environment:
```
$ virtualenv env
```

4. Activate the virtual environment:
```
$ source env/bin/activate
```

5. Install dependencies:
```
$ pip3 install -r requirements.txt
```

6. Make an account with [Active API](https://developer.active.com/docs/read/v2_Activity_API_Search) and get a free [API key](https://developer.active.com/member/register) <br/>
** when asked for which API that the application will use, check off the "Issue a new key for Activity Search API v2" box. That is all you will need.
Store the key in a file named 'secrets.sh':<br/>
![Secret](/static/ReadMe/secret_key.png)

7. Add the key to your environmental variables:
```
$ source secrets.sh
```

8. Create OnTrack database called 'races' with PostgreSQL:
```
$ createdb races
```

9. Seed database with data (optional - provided data is created by Faker, do this if you want to see what the rendered results will look like with more data) :
```
$ python3 seed_database.py
```
10. Run the app from the command line:
```
$ python3 server.py
```

Visit localhost:5000 on your browser. Enjoy!

## <a name="developer"></a>About the Developer

Before joining Hackbright Academy, Yuri was a successful classical violinist.  She had a full schedule of concerts to play every weekend and maintained a violin studio of pre-college students.  While she loved playing violin and teaching, she knew this was not her end game.  Her interest in software engineering sparked when she started learning HTML and CSS to build her personal website. She found similarities between learning programming languages and learning music, and suddenly she was hooked.  She continued to learn on her own, and after moving to the Bay Area, she enrolled in Hackbright to further deepen her knowledge.  Upon graduation, she looks forward to pursuing a career in software engineering and continuing building her skills.

Learn more about Yuri on her <a href="https://www.linkedin.com/in/yuri-uchida/">LinkedIn</a>
