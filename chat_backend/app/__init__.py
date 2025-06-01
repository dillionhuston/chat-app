from flask import Flask
from flask_cors import CORS

from models.db import db
from users.routes import user_blueprint  
from flask_jwt_extended import *

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'super-secret'

    db.init_app(app)
    jwt = JWTManager(app)
    CORS(app, resources={r"/*": {"origins": "*"}})


    with app.app_context():
        db.create_all()  

    app.register_blueprint(user_blueprint, url_prefix='/api/')

    return app
