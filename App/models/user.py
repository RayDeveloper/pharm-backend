from .database import db
from werkzeug.security import generate_password_hash, check_password_hash

#These are the roles for the users
#Customer - role=1 can add products, checkout and view orders
#Admins - role =2 Customer + manage products, orders and customers

# Should be Changed to an Enum similiarly to in Order
ACCESS = {
    'user': 1,
    'admin': 2
}

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False) 
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    allergies = db.Column(db.String(300))
    password = db.Column(db.String(120))
    role = db.Column(db.Integer, nullable = False)
    DOB = db.Column(db.DateTime, nullable = True)
    orders = db.relationship("Order",  back_populates="user", cascade="all,delete")
        
    def setPassword(self, password): 
        self.password = generate_password_hash(password, method="sha256")
    
    def checkPassword(self,password):
        return check_password_hash(self.password, password)
    
    def toDict(self):
        return{
            'first_name': self.first_name,
            'last_name': self.last_name,
            'DOB': self.DOB,
            'email': self.email,
            'role': self.role,
            'allergies': self.allergies,
            'orders': self.orders


        }
