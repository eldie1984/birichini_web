# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
import flask_excel as excel

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)
    Bootstrap(app)

    from app import models

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)
    excel.init_excel(app)


    return app
