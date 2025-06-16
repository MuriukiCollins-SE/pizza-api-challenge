from flask import Blueprint, jsonify, request
from server.models import Restaurant, RestaurantPizza
from server.extensions import db

restaurant_bp = Blueprint('restaurant_bp', __name__)

@restaurant_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([
        {
            "id": r.id,
            "name": r.name,
            "address": r.address
        } for r in restaurants
    ])

@restaurant_bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    pizzas = [
        {
            "id": rp.pizza.id,
            "name": rp.pizza.name,
            "ingredients": rp.pizza.ingredients
        }
        for rp in restaurant.restaurant_pizzas
    ]
    return jsonify({
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        "pizzas": pizzas
    })

@restaurant_bp.route('/restaurants', methods=['POST'])
def create_restaurant():
    data = request.get_json()
    name = data.get('name')
    address = data.get('address')
    if not name or not address:
        return jsonify({"error": "Name and address are required"}), 400
    restaurant = Restaurant(name=name, address=address)
    db.session.add(restaurant)
    db.session.commit()
    return jsonify({
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address
    }), 201

@restaurant_bp.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204