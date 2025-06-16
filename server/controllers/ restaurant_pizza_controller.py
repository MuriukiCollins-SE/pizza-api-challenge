from flask import Blueprint, jsonify, request
from server.app import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza

restaurant_pizza_bp = Blueprint('restaurant_pizza', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')
    
    # Validations
    errors = []
    if not (1 <= price <= 30):
        errors.append('Price must be between 1 and 30')
    if not Pizza.query.get(pizza_id):
        errors.append('Pizza not found')
    if not Restaurant.query.get(restaurant_id):
        errors.append('Restaurant not found')
    
    if errors:
        return jsonify({'errors': errors}), 400
    
    restaurant_pizza = RestaurantPizza(
        price=price,
        pizza_id=pizza_id,
        restaurant_id=restaurant_id
    )
    
    db.session.add(restaurant_pizza)
    db.session.commit()
    
    return jsonify(restaurant_pizza.to_dict()), 201