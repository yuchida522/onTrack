"""Models for running tracking app"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

db = SQLAlchemy()

#User table
class User(db.Model):

    """a user"""
    
    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    fname = db.Column(db.String,
                      nullable=False)
    lname = db.Column(db.String,
                      nullable=False)
    email = db.Column(db.String,
                      unique=True,
                      nullable=False)
    password = db.Column(db.String,
                         nullable=False)
    

    race = db.relationship('Race', secondary='current_races')

    def __repr__(self):

        return f'<User user_id={self.user_id}, email={self.email}>'


#race table
class Race(db.Model):

    """a race"""

    __tablename__ = 'races'

    race_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    race_name = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('cities.city_id'), nullable=False)
    race_url = db.Column(db.String, nullable=False)
    race_description = db.Column(db.Text, nullable=False)
    organization_name = db.Column(db.String, nullable=False)

    user = db.relationship('User', secondary='current_races')
    city = db.relationship('City')


    def __repr__(self):
        return f'<Race race_id={self.race_id}, race_name={self.race_name}>'

#city table
class City(db.Model):

    """a city"""
    
    __tablename__ = 'cities'

    city_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)

    city_name = db.Column(db.String, nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)

    race = db.relationship('Race')

    def __repr__(self):
        return f'<City city_id={self.city_id}, city_name={self.city_name}, zipcode={self.zipcode}>'


#current race table
class CurrentRace(db.Model):
    """a race and associated it to a users that saved the race to their account"""
    
    __tablename__ = 'current_races'

    current_race_id = db.Column(db.Integer,
                                primary_key=True,
                                autoincrement=True)
    race_id = db.Column(db.Integer, db.ForeignKey('races.race_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    signup_status = db.Column(db.String)
    notes = db.Column(db.String)

    #relationship- current race is the child of Race and User
    race = db.relationship('Race')
    user = db.relationship('User')


    def __repr__(self):
        return f'<CurrentRace race_id={self.current_race_id}, user_id={self.user_id}>'

class TrainingLog(db.Model):
    """a training log"""

    __tablename__ = 'training_logs'   

    training_log_id = db.Column(db.Integer,
                                primary_key=True,
                                autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    training_date = db.Column(db.Date, nullable=False)
    training_mileage = db.Column(db.Float, nullable=False, default=0) 
    training_effort = db.Column(db.String, nullable=False)
    training_comment = db.Column(db.String, nullable=False)
    training_run_time = db.Column(db.Interval, nullable=False, default=timedelta(hours=00, minutes=00, seconds=00))

    user = db.relationship('User')

    def __repr__(self):
        return f'<TrainingLog training_log_id={self.training_log_id}, user_id={self.user_id}>'



def connect_to_db(flask_app, db_uri='postgresql:///races', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    