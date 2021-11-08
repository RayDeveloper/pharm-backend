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


#get 20 products based on page
@product_views.route('/products', methods=["GET"])
def display_event():
    page = request.args.get('page')
    prodList = get_products_page(page)
    return jsonify(prodList)