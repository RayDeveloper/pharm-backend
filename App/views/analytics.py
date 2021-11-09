from flask import Blueprint, jsonify, request
from flask_jwt import jwt_required
import json

analytics_views = Blueprint('analytics_views', __name__, template_folder='../templates')

from App.controllers import (
get_monthly_sales,
get_monthly_income,
highest_selling_product,
highest_earning_product,
total_sales_category,

)

#get the monthly sales
@analytics_views.route('/display_monthly_sales', methods=["GET"])
@jwt_required()
def display_monthly_sales():
    user_date = request.args.get('date')
    salesList = get_monthly_sales(user_date)
    return jsonify(salesList)

#get the monthly income
@analytics_views.route('/display_monthly_income', methods=["GET"])
@jwt_required()
def display_monthly_income():
    user_date = request.args.get('date')
    incomeList = get_monthly_income(user_date)
    return jsonify(incomeList)

#get the highest selling product
@analytics_views.route('/display_highest_selling_product', methods=["GET"])
@jwt_required()
def display_highest_selling_product():
    high_product = highest_selling_product()
    return jsonify(high_product)

#get the highest earning product
@analytics_views.route('/display_highest_earning_product', methods=["GET"])
@jwt_required()
def display_highest_earning_product():
    high_earning = highest_earning_product()
    return jsonify(high_earning)

#get the total sales by category
@analytics_views.route('/display_total__sales_category', methods=["GET"])
@jwt_required()
def display_total__sales_category():
    total_category = total_sales_category()
    return jsonify(total_category)

