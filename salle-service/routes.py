from flask import Blueprint, jsonify, request
from database import db
from models import Item

bp = Blueprint("main", __name__)

@bp.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Service is up"}), 200

@bp.route("/items", methods=["GET"])
def get_items():
    items = Item.query.all()
    return jsonify([{"id": i.id, "name": i.name} for i in items])

@bp.route("/items", methods=["POST"])
def add_item():
    data = request.get_json()
    item = Item(name=data["name"])
    db.session.add(item)
    db.session.commit()
    return jsonify({"id": item.id, "name": item.name}), 201