"""CRUD operations"""

#importing models from model.py
from model import db, User, Race, City,CurrentRace, connect_to_db

def create_user(fname, lname, username, email, password):

    #creates a user
    user = User(fname=fname, lname=lname, username=username, email=email, password=password)

    #adds user to db
    db.session.add(user)
    db.session.commit()

    return user

def create_race(race_name, date, city, url, description, organization):
    
    #creates a race
    race = Race(race_name=race_name, date=date, city=city,  organization=organization)

    #add race to db
    db.session.add(race)
    db.session.commit()

    return race

def create_city(name, zipcode):
    
    city = City(name=name, zipcode=zipcode)

    #add city to db
    db.session.add(city)
    db.session.commit()

    return city

def create_current_race(username, race, signup_status):
    
    current_race = CurrentRace(username=username, race=race, signup_status=signup_status)

    #add current_race to db
    db.session.add(current_race)
    db.session.commit()

    return current_race
