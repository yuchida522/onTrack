"""CRUD operations"""

from model import db, User, Race, City, CurrentRace, TrainingLog, connect_to_db
from sqlalchemy.sql import functions

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

def create_current_race(race, user_id, signup_status):
    
    current_race = CurrentRace(race=race,
                               user_id=user_id,
                               signup_status=signup_status)

    #add current_race to db
    db.session.add(current_race)
    db.session.commit()

    return current_race


def create_training_log(user_id, training_date, training_mileage, training_effort, training_comment, training_run_time):

    training_log = TrainingLog(user_id=user_id,
                               training_date=training_date,
                               training_mileage=training_mileage, 
                               training_effort=training_effort,
                               training_comment=training_comment,
                               training_run_time=training_run_time)

    #add the new training log to db
    db.session.add(training_log)
    db.session.commit()

    return training_log


 
def get_user_by_email(email):
    """searches for user object by email"""

    return User.query.filter(User.email == email).first()


def get_user_by_user_id(user_id):

    return User.query.filter(User.user_id == user_id).first()


######################## CURRENT RACE ENTRIES#################################


def get_currentraces_by_id(user_id):
    """searches for current races that the user has saved in their account"""

    return CurrentRace.query.filter(CurrentRace.user_id==user_id).all()
    

def get_saved_race(current_race_id):
    """finds the current race saved"""

    return CurrentRace.query.filter(CurrentRace.current_race_id==current_race_id).first()


def update_race_signup_status(current_race_id, new_signup_status):
    """update saved race signup status"""

    race_to_update = CurrentRace.query.filter(CurrentRace.current_race_id==current_race_id).first()

    race_to_update.signup_status = new_signup_status

    db.session.commit() 



def delete_saved_race(current_race_id):
    """deletes a race saved by the user"""

    current_race = CurrentRace.query.filter(CurrentRace.current_race_id==current_race_id).first()

    db.session.delete(current_race)
    db.session.commit()



######################## TRAINING LOG ENTRIES ##################################


def get_training_log_by_userid(user_id):
    """function that grabs all the training logs associated with the account (look up by user_id)"""

    return TrainingLog.query.filter(TrainingLog.user_id == user_id).order_by(TrainingLog.training_date).all()



def get_total_mileage(user_id):
    """function that return total mileage ran by the user"""

    return TrainingLog.query.with_entities(functions.sum(TrainingLog.training_mileage)).filter(TrainingLog.user_id == user_id).first()

    
def get_total_number_of_runs(user_id):
    """function that return total mileage ran by the user"""

    return TrainingLog.query.filter(TrainingLog.user_id == user_id).count()




def get_training_log_by_log_id(training_log_id):

    return TrainingLog.query.filter(TrainingLog.training_log_id == training_log_id).first()


def delete_training_log(training_log_id):

    training_log = TrainingLog.query.filter(TrainingLog.training_log_id == training_log_id).first()

    db.session.delete(training_log)
    db.session.commit()


def update_training_log(training_log_id, new_date, new_mileage, new_effort, new_comment):

    training_log_to_update = TrainingLog.query.filter(TrainingLog.training_log_id == training_log_id).first()

    training_log_to_update.training_date = new_date
    training_log_to_update.training_mileage = new_mileage
    training_log_to_update.training_effort = new_effort
    training_log_to_update.training_comment = new_comment

    db.session.commit()



if __name__ == '__main__':
    from server import app
    connect_to_db(app)