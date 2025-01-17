from App.models import User
from App.database import db

from App.models import Exercise
from App.models import ExerciseSet

# from App.controllers import *

def create_user(username, email, password):
    newuser = User(username=username, email=email, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

# methods to add, delete etc exerciseSets
def add_exerciseSet(name, user_id, exercise_id):

    exercise = Exercise.query.get(exercise_id)
    # exercise = get_exercise_by_id(exercise_id)

    if(exercise):
        try:
            # print('test1')
            # exerciseSet = create_exerciseSet(name=name, user_id=user_id, exercise_id=exercise_id)
            # newExerciseSet = ExerciseSet.query.filter_by(name=name).first()

            # if newExerciseSet is not None:
            #     # add to the set
            #     test = 1
            # else:
            newExerciseSet = ExerciseSet(user_id=user_id, exercise_id=exercise_id, name=name)
            db.session.add(newExerciseSet)
            db.session.commit()

            # print('test2')
            return exerciseSet
        except Exception:
            # print('test3')
            db.session.rollback()
            return None
        return None

def delete_exerciseSet(exerciseSet_id):

    exerciseSets = ExerciseSet.query.filter_by(id=exerciseSet_id).all()

    if exerciseSets is not None:
        for exerciseSet in exerciseSets:
            db.session.delete(exerciseSet)
        
            db.session.commit()
        return True
    return None
    
    
def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
    
