from App.models import User

#This method is used by /auth view to check if user-sent credentials are valid
def authenticate(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.checkPassword(password):
        return user

#Payload is a dictionary which is passed to the function by Flask JWT
def identity(payload):
    return User.query.get(payload['identity'])

#testings