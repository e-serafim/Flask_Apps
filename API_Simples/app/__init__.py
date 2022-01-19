from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SECRET_KEY'] = "secret"

    api = Api(app, prefix='/api')
    db.init_app(app)
    login_manager.init_app(app)

    from app import routes
    routes.init_app(app)

    from app.resources.usuarios import Usuarios
    api.add_resource(Usuarios, '/usuarios')

    return app
