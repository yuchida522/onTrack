"""CRUD operations"""

from model import db, User, Race, City, CurrentRace, connect_to_db

def create_user(fname, lname, username, email, password):

    #creates a user
    user = User(fname=fname, lname=lname, username=username, email=email, password=password)

    #adds user to db
    db.session.add(user)
    db.session.commit()

    return user

def create_race(race_name, date, race_url, race_description, organization_name):
    
    #creates a race
    race = Race(race_name=race_name, date=date,
                race_url=race_url, race_description=race_description, 
                organization_name=organization_name)

    #add race to db
    db.session.add(race)
    db.session.commit()

    return race

def create_city(city_name, zipcode):
    
    city = City(city_name=city_name, zipcode=zipcode)

    #add city to db
    db.session.add(city)
    db.session.commit()

    return city

def create_current_race(race, user, signup_status):
    
    current_race = CurrentRace(race=race, user=user, signup_status=signup_status)

    #add current_race to db
    db.session.add(current_race)
    db.session.commit()

    return current_race

if __name__ == '__main__':
    from server import app
    connect_to_db(app)