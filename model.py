from flask import SQLAlchemy

db = SQLAlchemy

#User table
class User(db.Model):
    
    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        primary_key=True)
    username = db.Column(db.String,
                         unique=True,
                         nullable=False)
    email = db.Column(db.String,
                      unique=True,
                      nullable=False)
    password = db.Column(db.String,
                         nullable=False)
    fname = db.Column(db.String,
                      nullable=False)
    lname = db.Column(db.String,
                      nullable=False)

    current_race = db.relationship('CurrentRace')

    def __repr__(self):

        return f'<User user_id={self.user_id}, email={self.email}>'


#race table
class Race(db.Model):
    
    __tablename__ = 'race'

    race_id = db.Column(db.Integer,
                        primary_key=True)
    race_name = db.Column(db.String)
    date = db.Column(db.DateTime)
    city_id = db.Column(db.Integer, db.ForeignKey('city.city_id'))
    race_url = db.Column(db.String)
    race_description = db.Column(db.Text)
    distance_length_id = db.Column(db.Integer, db.ForeignKey('distance_length.distance_length_id'))
    address = db.Column(db.String)
    organization_name = db.Column(db.String)

    current_race = db.relationship('current_race')


    def __repr__(self):
        return f'<Race race_id={self.race_id}, race_name={self.race_name}>'

#city table
class City(db.Model):
    
    __tablename__ = 'city'

    city_id = db.Column(db.Integer,
                        primary_key=True)
    city_name = db.Column(db.String, nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<City city_id={self.city_id}, city_name={self.city_name}, zipcode={self.zipcode}>'


#distance table
class DistanceLength(db.Model):
    
    __tablename__ = 'distance_length'

    distance_length_id = db.Column(db.Integer,
                                   primary_key=True)
    distance_length = db.Column(db.Integer)

    def __repr__(self):
        return f'<DistanceLength distance_length_id={self.distance_length_id}, distance_length={self.distance_length}>'


#current race table
class CurrentRace(db.Model):
    
    __tablename__ = 'current_race'

    current_race_id = db.Column(db.Integer,
                                primary_key=True)
    race_id = db.Column(db.Integer, db.ForeignKey('race.race_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    signup_status = db.Column(db.Boolean)

    #relationship- current race is the child of Race and User
    race = db.relationship('Race')
    user = db.relationship('User')


    def __repr__(self):
        return f'<CurrentRace race_id={self.race_id}, user_id={self.user_id}>'


# signup status table?

# past race table?

#  class PastRace(db.Model):
#     __tablename__ = 'past_races'
#    past_race_id = db.Column(db.Integer,
#                                 primary_key=True)
#     user_id = db.Column()                          
#     race_id = db.Column(db.Integer, db.ForeignKey('race.race_id'))



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