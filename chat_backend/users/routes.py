from flask import Flask, jsonify, request, send_file, Blueprint
from models.user import User
from users.controller import UserController

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'}), 200


@user_blueprint.route('/signup', methods=['POST'])
def signup():
    details = request.get_json()
    username = details.get('usernmae')
    password = details.get('password')
    email = details.get('email')
    User.add_user(username, password, email)
    return jsonify({'message', 'succes: user signed up scuessfilly '})


@user_blueprint.route('/login', methods=['POST'])
def login():
    details = request.get_json()
    username = details.get('username')
    password = details.get("password")
    UserController.authenticate_user(username, password)
    return jsonify({'message,' : "success, user logged in"}), 200


