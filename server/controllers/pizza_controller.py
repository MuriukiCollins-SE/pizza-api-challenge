from flask import Blueprint, request, jsonify
from server.extensions import db
from server.models import Pizza

pizza_bp = Blueprint('pizza_bp', __name__)

@pizza_bp.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    # If no pizzas, add a demo one for functionality
    if not pizzas:
        demo = Pizza(name="Demo Pizza", ingredients="Demo Ingredients")
        db.session.add(demo)
        db.session.commit()
        pizzas = [demo]
    return jsonify([
        {
            "id": p.id,
            "name": p.name,
            "ingredients": p.ingredients
        } for p in pizzas
    ])

@pizza_bp.route('/pizzas/<int:id>', methods=['GET'])
def get_pizza_by_id(id):
    pizza = Pizza.query.get(id)
    if not pizza:
        return jsonify({"error": "Pizza not found"}), 404
    return jsonify({
        "id": pizza.id,
        "name": pizza.name,
        "ingredients": pizza.ingredients
    })

@pizza_bp.route('/pizzas', methods=['POST'])
def create_pizza():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 415
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid or missing JSON body"}), 400
    name = data.get('name')
    ingredients = data.get('ingredients')
    if not name or not ingredients:
        return jsonify({"error": "Name and ingredients are required"}), 400
    pizza = Pizza(name=name, ingredients=ingredients)
    db.session.add(pizza)
    db.session.commit()
    return jsonify({
        "id": pizza.id,
        "name": pizza.name,
        "ingredients": pizza.ingredients
    }), 201