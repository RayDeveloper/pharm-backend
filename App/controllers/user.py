from App.models import User
from App.models.database import db

# create USER
def create_user(firstname, lastname, email, password, allergy, role):
    newUser = User(first_name=firstname, last_name=lastname, email=email, allergies = allergy, role = role)
    newUser.setPassword(password)
    db.session.add(newUser)
    db.session.commit()
    print("User successfully created")
    return newUser

# get user by email
def get_user(email):
    print("getting user")
    user = User.query.filter_by(email=email).first()
    return user

# get all users - used by admin in - manage users
def get_users():
    print('get_users')
    users = User.query.all()
    list_of_users = []
    if users:
        list_of_users = [u.toDict() for u in users]
    return list_of_users

    # get the order history for all users, even admins
def get_users_orders_history():
    print('Get order history for users')
    user_history = User.query.all()
    list_of_users = []
    if user_history:
        list_of_users = [c.toDict() for c in user_history]
    return list_of_users