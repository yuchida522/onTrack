"""CRUD operations"""

from model import db, User, Race, City, CurrentRace, TrainingLog, connect_to_db
from sqlalchemy.sql import functions

################################################################################
#                                                                              #
#                   CRUD FUNCTIONS FOR ADDING DATA TO DB                       #
#                                                                              #
################################################################################


def create_user(fname, lname, username, email, password):
    """function that creates a user and saves in db"""

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
    """function that saves city information of the race from API call to db"""
    
    exists = City.query.filter_by(city_name=city_name).first()
    city = City(city_name=city_name, zipcode=zipcode)

    if not exists:
    
        #add city to db
        db.session.add(city)
        db.session.commit()

        return city
    else:
        return exists


def create_current_race(race, user_id, signup_status, completed_status, notes):
    """function that takes race information and saves in db"""
    
    current_race = CurrentRace(race=race,
                               user_id=user_id,
                               signup_status=signup_status,
                               completed_status=completed_status,
                               notes=notes)

    #add current_race to db
    db.session.add(current_race)
    db.session.commit()

    return current_race


def create_training_log(user_id, training_date, training_mileage, training_effort, training_comment, training_run_time):
    """function that creates and saves a training log to db"""

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


################################################################################
#                                                                              #
#                     USER AUTHENTICATION CRUD FUNCTION                        #
#                                                                              #
################################################################################

 
def get_user_by_email(email):
    """queries for user object by email"""

    return User.query.filter(User.email == email).first()


def get_user_by_user_id(user_id):
    """queries user by user_id"""

    return User.query.filter(User.user_id == user_id).first()


################################################################################
#                                                                              #
#                       SAVED RACES CRUD FUNCTIONS                             #
#                                                                              #
################################################################################


def get_currentraces_by_id(user_id):
    """searches for current races that the user has saved in their account"""

    return CurrentRace.query.filter(CurrentRace.user_id==user_id).all()
    

def get_saved_race(current_race_id):
    """find saved race by its ID"""

    return CurrentRace.query.filter(CurrentRace.current_race_id==current_race_id).first()


def update_saved_race(current_race_id, new_signup_status, new_completed_status, new_notes):
    """update status and comments on a saved race"""

    race_to_update = CurrentRace.query.filter(CurrentRace.current_race_id==current_race_id).first()

    race_to_update.signup_status = new_signup_status
    race_to_update.completed_status = new_completed_status
    race_to_update.notes = new_notes

    db.session.commit() 



def delete_saved_race(current_race_id):
    """deletes a race saved by the user"""

    current_race = CurrentRace.query.filter(CurrentRace.current_race_id==current_race_id).first()

    db.session.delete(current_race)
    db.session.commit()



################################################################################
#                                                                              #
#                        TRAINING LOG CRUD FUNCTIONS                           #
#                                                                              #
################################################################################


def get_training_log_by_userid(user_id):
    """function that grabs all the training logs associated with the account (look up by user_id)"""

    return TrainingLog.query.filter(TrainingLog.user_id == user_id).order_by(TrainingLog.training_date).all()



def get_total_mileage(user_id):
    """function that return total mileage ran by the user"""

    total_mileage = db.session.query(functions.sum(TrainingLog.training_mileage)).filter(TrainingLog.user_id == user_id).first()[0]

    if total_mileage is None:
        return 0
    
    return total_mileage


def get_total_number_of_runs(user_id):
    """function that return total mileage ran by the user"""

    return TrainingLog.query.filter(TrainingLog.user_id == user_id).count()


def get_avg_run_time(user_id):
    """funtion that caculates average pace by dividing the total mileage and time"""
    
    total_mileage = db.session.query(functions.sum(TrainingLog.training_mileage)).filter(TrainingLog.user_id == user_id).first()[0]
    total_time = db.session.query(functions.sum(TrainingLog.training_run_time)).filter(TrainingLog.user_id == user_id).first()[0]

    if total_mileage is None and total_time is None:
        return '00:00:00'
    else:
        return convert_deltatime_to_time(total_time / total_mileage)
    #query for total mileage
    #query for total time
    #divide sum(mileage) by sum(time)

def convert_deltatime_to_time(timedelta_obj):
    """function that converts deltatime to readable time"""

    total_seconds = timedelta_obj.total_seconds()
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    remaining_seconds = remaining_seconds % 60

    return f'{round(hours)}0:{round(minutes)}:0{round(remaining_seconds)}'


def get_training_log_by_log_id(training_log_id):
    """function that queries for specific training log by its id"""

    return TrainingLog.query.filter(TrainingLog.training_log_id == training_log_id).first()


def delete_training_log(training_log_id):
    """function that deletes a specific training log from the db"""

    training_log = TrainingLog.query.filter(TrainingLog.training_log_id == training_log_id).first()

    db.session.delete(training_log)
    db.session.commit()


def update_training_log(training_log_id, new_date, new_mileage, new_effort, new_comment, new_time):
    """function that updates an exisiting training log in db"""

    training_log_to_update = TrainingLog.query.filter(TrainingLog.training_log_id == training_log_id).first()

    training_log_to_update.training_date = new_date
    training_log_to_update.training_mileage = new_mileage
    training_log_to_update.training_effort = new_effort
    training_log_to_update.training_comment = new_comment
    training_log_to_update.training_run_time = new_time

    db.session.commit()




if __name__ == '__main__':
    from server import app
    connect_to_db(app)