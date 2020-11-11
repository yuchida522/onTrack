"""CRUD operations"""

from model import db, User, Race, City, CurrentRace, TrainingLog, connect_to_db

def create_user(fname, lname, username, email, password):

    #creates a user
    user = User(fname=fname, lname=lname, username=username, email=email, password=password)

    #adds user to db
    db.session.add(user)
    db.session.commit()

    return user

def create_race(race_name, date, city, race_url, race_description, organization_name):
    
    #creates a race
    race = Race(race_name=race_name,
                date=date,
                city=city,
                race_url=race_url,
                race_description=race_description, 
                organization_name=organization_name)

    #add race to db
    db.session.add(race)
    db.session.commit()

    return race

#TODO: refactor how to handle exisiting cities
def create_city(city_name, zipcode):
    
    exists = City.query.filter_by(city_name=city_name).first()
    city = City(city_name=city_name, zipcode=zipcode)

    if not exists:
    
        #add city to db
        db.session.add(city)
        db.session.commit()

        return city
    else:
        return exists

def create_current_race(race, user, signup_status):
    
    current_race = CurrentRace(race=race, user=user, signup_status=signup_status)

    #add current_race to db
    db.session.add(current_race)
    db.session.commit()

    return current_race

def create_training_log(user, training_date, training_mileage, training_effort, training_comment):

    training_log = TrainingLog(user=user,
                               training_date=training_date,
                               training_mileage=int(training_mileage), 
                               training_effort=training_effort,
                               training_comment=training_comment)

    #add the new training log to db
    db.session.add(training_log)
    db.session.commit()

    return training_log


 #search user object by email
def get_user_by_email(email):

    return User.query.filter(User.email == email).first()


#searches for current races that the user has saved in their account
def get_currentraces_by_id(user_id):


    return CurrentRace.query.filter(CurrentRace.user_id==user_id).all()
    

    # return db.session.query(User, Race).filter(User.user_id == user_id, CurrentRace.race_id == Race.race_id).all()



#function that grabs all the training logs associated with the account (look up by user_id)
def get_training_log_by_userid(user_id):

    return TrainingLog.query.filter(TrainingLog.user_id == user_id).order_by(TrainingLog.training_date).all()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)