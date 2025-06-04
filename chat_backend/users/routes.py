import json
from flask import Blueprint, jsonify, request
from users.controller import UserController

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'}), 200


@user_blueprint.route('/signup', methods=['POST'])
def signup():
    # Get json, return  400 if invalid
    payload = request.get_json(silent=True)
    if not payload:
        return jsonify({'error': 'Invalid or missing JSON payload'}), 400
    username = payload.get('username')
    password = payload.get('password')
    email = payload.get('email')
    response, status = UserController.create_user(username, email, password)
    return jsonify(response), status


@user_blueprint.route('/login', methods=['POST'])
def login():
    # Get json, return  400 if invalid
    payload = request.get_json(silent=True)
    if not payload:
        return jsonify({'error': 'Invalid or missing JSON payload'}), 400
    username = payload.get('username')
    password = payload.get('password')
    response, status = UserController.authenticate_user(username, password)
    return jsonify(response), status