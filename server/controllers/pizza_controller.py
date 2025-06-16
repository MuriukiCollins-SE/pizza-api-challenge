from flask import Blueprint, request, jsonify
from server.extensions import db
from server.models import Pizza

pizza_controller = Blueprint('pizza_controller', __name__)

@pizza_controller.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([pizza.serialize() for pizza in pizzas])

@pizza_controller.route('/pizzas', methods=['POST'])
def add_pizza():
    data = request.get_json()
    new_pizza = Pizza(**data)
    db.session.add(new_pizza)
    db.session.commit()
    return jsonify(new_pizza.serialize()), 201

@pizza_controller.route('/pizzas/<int:pizza_id>', methods=['GET'])
def get_pizza(pizza_id):
    pizza = Pizza.query.get_or_404(pizza_id)
    return jsonify(pizza.serialize())

@pizza_controller.route('/pizzas/<int:pizza_id>', methods=['PUT'])
def update_pizza(pizza_id):
    data = request.get_json()
    pizza = Pizza.query.get_or_404(pizza_id)
    for key, value in data.items():
        setattr(pizza, key, value)
    db.session.commit()
    return jsonify(pizza.serialize())

@pizza_controller.route('/pizzas/<int:pizza_id>', methods=['DELETE'])
def delete_pizza(pizza_id):
    pizza = Pizza.query.get_or_404(pizza_id)
    db.session.delete(pizza)
    db.session.commit()
    return '', 204

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