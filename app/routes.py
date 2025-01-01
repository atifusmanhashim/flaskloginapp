from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from app.models import User, Base
from app import SessionLocal

api = Blueprint('api', __name__)

@api.route('/users', methods=['GET'])
def get_users():
    """Get all users."""
    session = SessionLocal()
    try:
        users = session.query(User).all()
        return jsonify([{"id": user.id, "name": user.name, "email": user.email} for user in users])
    finally:
        session.close()

@api.route('/users', methods=['POST'])
def create_user():
    """Create a new user."""
    data = request.get_json()
    session = SessionLocal()
    try:
        new_user = User(name=data['name'], email=data['email'])
        session.add(new_user)
        session.commit()
        return jsonify({"id": new_user.id, "name": new_user.name, "email": new_user.email}), 201
    except SQLAlchemyError as e:
        session.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        session.close()
