from models.db import db
from models.user import User
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask import Flask, jsonify, request, send_file


class UserController():
    def create_user(username, email, password):
        # DO checks 
        if not all([username, email, password]):
            return {"error": "Missing required fields"},400
        
        if User.query.filter_by(email=email).first():
            return {"error:" "email registered "},400
        
        User.add_user(username, email, password)
        return {"message": "user added"}, 200


    def authenticate_user(username, password):
        """
        Handles user login logic.
        Returns a tuple: (response_dict, status_code)
        """
        user = User.query.filter_by(username=username).first()
        if user & User.check_password(password, user.password):
            token = create_access_token(identity=str(user.id))
            return jsonify({'message': 'Success', 'token': token, 'user_id': str(user.id)}), 200
        else:
            return jsonify({'message': 'error:  notoken '}),404

        

        