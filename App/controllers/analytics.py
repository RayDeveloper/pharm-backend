from App.models import ( Order )
from App.models import ( ProductOrder )
from App.models import ( Product )
from App.models.database import db
from flask import redirect, render_template, request, session, url_for
from App.models import Product
from App import parse
from sqlalchemy import func
import json



# gets the monthly sales
def get_monthly_sales(date):
    print('Monthly sales')
    sales = Order.query.filter_by(Order.date_placed == date).all()
    list_of_sales = []
    if sales:
        list_of_sales = [p.toDict() for s in sales]
    return list_of_sales

# get the monthly income
def get_monthly_income(date):
    print('Monthly Income')
    income = Order.query.filter_by(Order.date_placed == date,func.sum(order_total)).all()
    return income

# get the highest selling product
def highest_selling_product():
    print('Highest selling product')
    high_selling_product = ProductOrder.query.filter_by(status== "Completed",func.count(product)).max()
    return high_selling_product

# get the highest earning product
def highest_earning_product():
    print ('Highest earning product')
    #high_earning_product = productOrder.query.filter_by(status=="Completed",func.max(current_price) ).first()
    high_earning_product = db.session.query(Product.product_name,fuc.sum(ProductOrder.product_id)
    ).join(Product).join(ProductOrder).filter(productOrder.status=="Completed").group_by(Product.name).order_by(ProductOrder.product_id).first()
    return high_earning_product

#Total sales by category
def total_sales_category():
    print('Sales by Category')
    total_sales_category = db.session.query(Product.category,fuc.sum(productOrder.current_price)
    ).join(Product).join(ProductOrder).filter(productOrder.status=="Completed").group_by(Product.category).all()
    return total_sales_category




    
