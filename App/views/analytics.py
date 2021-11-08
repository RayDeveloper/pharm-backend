from flask import Blueprint, jsonify, request
from flask_jwt import jwt_required

customer_views = Blueprint('analytics_views', __name__, template_folder='../templates')

from App.controllers import (
get_monthly_sales,
get_monthly_income,
highest_selling_product,
highest_earning_product,
total_sales_category
)


#get the monthly sales
@product_views.route('/products', methods=["GET"])
@jwt_required()
def display_monthly_sales():
    user_date = request.args.get('date')
    salesList = get_monthly_sales(date)
    return jsonify(salesList)

#get the monthly income
@product_views.route('/products', methods=["GET"])
@jwt_required()
def display_monthly_income():
    user_date = request.args.get('date')
    incomeList = get_monthly_income(date)
    return jsonify(incomeList)

#get the highest selling product
@product_views.route('/products', methods=["GET"])
@jwt_required()
def display_highest_selling_product():
    high_product = highest_selling_product()
    return jsonify(high_product)

#get the highest earning product
@product_views.route('/products', methods=["GET"])
@jwt_required()
def display_highest_earning_product():
    high_earning = highest_earning_product()
    return jsonify(high_earning)

#get the total sales by category
@product_views.route('/products', methods=["GET"])
@jwt_required()
def display_total__sales_category():
    total_category = total_sales_category()
    return jsonify(total_category)

