# import flask
from flask import Flask

# for styling css
from flask_bootstrap import Bootstrap

# SQl toolkit for python
from flask_sqlalchemy import SQLAlchemy

# import config options form config
from config import config_options

bootstrap = Bootstrap()

db = SQLAlchemy()


def create_app(config_name):

    # intiating flask us a app
    app = Flask(__name__)

    # getting bootstrap form app
    bootstrap.init_app(app)

    # Initializing flask extensions
    db.init_app(app)

    # allows to get settings form config
    app.config.from_object(config_options[config_name])

    # Registering the main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # blueprint of the authnication
    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint, url_prefix='/authenticate')

    return app
