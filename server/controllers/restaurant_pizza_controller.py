from flask import Blueprint, request, jsonify
from server.models import RestaurantPizza, Pizza, Restaurant
from server.extensions import db

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    if not request.is_json:
        return jsonify({'errors': ['Content-Type must be application/json']}), 415
    data = request.get_json(silent=True)
    if not data:
        return jsonify({'errors': ['Invalid or missing JSON body']}), 400

    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    errors = []
    # validate price first and return immediately if invalid
    if price is None or not isinstance(price, int) or not (1 <= price <= 30):
        return jsonify({'errors': ['Price must be between 1 and 30']}), 400

    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)
    if not pizza:
        errors.append('Pizza not found')
    if not restaurant:
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

    return jsonify({
        "id": restaurant_pizza.id,
        "price": restaurant_pizza.price,
        "pizza_id": restaurant_pizza.pizza_id,
        "restaurant_id": restaurant_pizza.restaurant_id,
        "pizza": {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        },
        "restaurant": {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address
        }
    }), 201

@restaurant_pizza_bp.route('/restaurant_pizzas/<int:id>', methods=['GET'])
def get_restaurant_pizza_by_id(id):
    rp = RestaurantPizza.query.get(id)
    if not rp:
        return jsonify({"error": "RestaurantPizza not found"}), 404
    return jsonify({
        "id": rp.id,
        "price": rp.price,
        "pizza_id": rp.pizza_id,
        "restaurant_id": rp.restaurant_id,
        "pizza": {
            "id": rp.pizza.id,
            "name": rp.pizza.name,
            "ingredients": rp.pizza.ingredients
        },
        "restaurant": {
            "id": rp.restaurant.id,
            "name": rp.restaurant.name,
            "address": rp.restaurant.address
        }
    }), 200

@restaurant_pizza_bp.route('/restaurant_pizza', methods=['GET'])
def get_restaurant_pizzas():
    associations = RestaurantPizza.query.all()
    return jsonify([{'restaurant_id': assoc.restaurant_id, 'pizza_id': assoc.pizza_id} for assoc in associations]), 200

@restaurant_pizza_bp.route('/restaurant_pizza/<int:id>', methods=['DELETE'])
def delete_restaurant_pizza(id):
    association = RestaurantPizza.query.get_or_404(id)
    db.session.delete(association)
    db.session.commit()
    return jsonify({'message': 'Association deleted'}), 200