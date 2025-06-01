import uuid
import os

from models.db import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from Crypto.Cipher import AES

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    key = db.Column(db.String(32), nullable=False)


    #TODO add rotating key each chat
    @staticmethod
    def add_user(username, email, password):
        print(f"addind user{username}") # debug
        newuser = User(
            id=str(uuid.uuid4()),
            username = username,
            password = generate_password_hash(password),
            email = email, 
            key = os.urandom(32).hex()[:32]  
       )
        db.session.add(newuser)   
        db.session.commit()
        db.session.close()   
        return newuser
    
    @staticmethod
    def check_password(password, pwhash):
        user_pw =  check_password_hash(password=password, pwhash=pwhash)
        if user_pw: return
            
    def get_key(self):
        return self.key
    
        
    
