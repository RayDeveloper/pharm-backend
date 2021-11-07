from App.models import ( ProductOrder )
from App.models.database import db

# This creates an association between an order and its products
def create_order_product(order, product):
    newOrderProduct = ProductOrder(order_id = order.id, product_id = product.id,)
    print("Successfully Created")
    db.session.add(newOrderProduct)
    db.session.commit()
    return newOrderProduct
