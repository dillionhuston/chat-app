from flask import Flask
from users.routes import user_blueprint

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'super-secret'

    app.register_blueprint(user_blueprint, url_prefix='/api/users')

    return app
