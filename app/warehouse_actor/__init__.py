# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# local imports
from config import app_config

db = SQLAlchemy()


def create_app(config_name):
    """Construct the core application."""
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    migrate = Migrate(app, db)

    from app.warehouse_actor import models

    # @app.route("/")
    # def hello_world():
    #     return "Hello, World!"

    # with app.app_context():
    #     # Imports
    #     from . import routes

    #     # Create tables for our models
    #     db.create_all()

    return app
