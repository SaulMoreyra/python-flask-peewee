from flask import Blueprint, jsonify, request
from ..application import UserService

bp = Blueprint('users', __name__)
user_service = UserService()


@bp.route('/users')
def get_users():
    result = user_service.find_all()
    return jsonify(result)


@bp.route('/users/<int:user_id>')
def get_user(user_id: int):
    user = user_service.find_by_id(user_id)
    return jsonify(user)


@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    result = user_service.create_one(
        username=data.get('username'),
        password=data.get('password'),
        email=data.get('email'),
        join_date=data.get('join_date'),
    )
    return jsonify(result)
