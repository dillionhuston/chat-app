import uuid
import os
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from models.db import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    key = db.Column(db.String(32), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


    @staticmethod
    def add_user(username, email, password):
        print(f"[DEBUG] Adding user: {username}") 

        new_user = User(
            id=str(uuid.uuid4()),
            username=username,
            email=email,
            password=generate_password_hash(password),
            key=os.urandom(32).hex()[:32]  # this soon wont be used 
        )
        db.session.add(new_user)
        return new_user

    @staticmethod
    def check_password(password, hashed_password):
        return check_password_hash(hashed_password, password)

    def get_key(self):
        return self.key