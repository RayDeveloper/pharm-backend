from App.models import ( User )
from App.models.database import db

#gets customers by filtering users based on their roles
# customer - role=1
def get_customers():
    print('get all customers')
    customers = User.query.filter_by(role = 1)
    list_of_customers = []
    if customers:
        list_of_customers = [c.toDict() for c in customers]
    return list_of_customers

# This is used for searching through customers by their attributes in
#admin - manage customers on the frontend
def get_customers_by_term(term):
    list_of_customers = []
    customers = User.query.filter(
        (User.role.contains(1)) &
        (User.allergies.contains(term) 
        | User.email.contains(term)
        | User.first_name.contains(term)
        | User.last_name.contains(term))
    )
    if customers:
        list_of_customers = [c.toDict() for c in customers]
    return list_of_customers

#method for deleting customer at /delete-customer endpoint
def delete_customer_by_email(email):
    print("deleting customer")
    customer = User.query.filter(User.email == email).first()
    if customer:
        db.session.delete(customer)
        db.session.commit()
        return True
    return False

