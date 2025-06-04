
import re
from models.db import db
from models.user import User
from flask import jsonify
from flask_jwt_extended import create_access_token

class UserController:
    @staticmethod
    def create_user(username, email, password):
        # validate all inputs in one go
        errors = []
        if not all([username, email, password]):
            errors.append("Hey, you forgot to fill in all the fields!")
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d).{8,}$', password):
            errors.append("Password needs to be 8+ characters with both letters and numbers.")
        if User.query.filter_by(email=email).first():
            errors.append("That email’s already in use. Try another one!")
        if User.query.filter_by(username=username).first():
            errors.append("That username’s taken. Pick a different one!")

        #  first error if any
        if errors:
            return {"error": errors[0]}, 400

        try:
            print(f"[DEBUG] Creating user: {username}")
            new_user = User.add_user(username, email, password)
            db.session.commit()
            return {
                "message": f"Welcome aboard, {username}! Your account is ready.",
                "user_id": str(new_user.id)
            }, 201
        except Exception as e:
            db.session.rollback()
            print(f"[ERROR] Failed to create user: {str(e)}")
            return {"error": f"Oops, something broke while creating your account: {str(e)}"}, 500


    @staticmethod
    def authenticate_user(username, password):
        # validate 
        if not all([username, password]):
            return {"error": "Please provide both username and password."}, 400

        user = User.query.filter_by(username=username).first()
        # check user and password
        return (
            {
                "message": "Login successful! Here`s your token.",
                "token": create_access_token(identity=str(user.id)),
                "user_id": str(user.id)
            },
            200
        ) if user and User.check_password(password, user.password) else (
            {"error": "Invalid username or password. Give it another shot!"},
            401
        )
