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
    #app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config["SQLALCHEMY_DATABASE_URI"]='postgresql://naoispmdeotyla:f6c79e30d9f22deb29ca444431e0c392a5111feb17b3df37b088c74fd65277ed@ec2-44-197-128-108.compute-1.amazonaws.com:5432/d18tik4chetjgk'
    db.init_app(app)
    migrate = Migrate(app, db)
    Bootstrap(app)

    from app import models

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)
    excel.init_excel(app)


    return app
