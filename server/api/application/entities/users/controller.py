from flask import Blueprint, jsonify, request

from application.entities.users.model import User
from application.entities.users.repository import UsersRepository

users_controller = Blueprint('users_controller', __name__)


@users_controller.route('/api/users', methods=['GET'])
def get_all_users():
    users = UsersRepository.get_all_users()
    return jsonify(users)


@users_controller.route('/api/users/<user_id>/', methods=['GET'])
def get_by_id(user_id: str):
    user = UsersRepository.get_user_by_id(user_id)
    return jsonify(user)


@users_controller.route('/api/users/new/<nickname>/<int:avatar_id>/', methods=['GET'])
def post_user(nickname: str, avatar_id: int):
    user = UsersRepository.create_new_user(nickname, avatar_id)
    user_json = user.to_json
    return jsonify(user_json)


@users_controller.route('/api/users/update/<user_id>/<user_name>/<int:avatar_id>/', methods=['GET'])
def put_user(user_id: str, user_name: str, avatar_id: int):
    user = User(user_name, avatar_id)
    user.user_id = user_id
    updated_user = UsersRepository.update_user(user)
    user_json = updated_user.to_json
    return jsonify(user_json)

