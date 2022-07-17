from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_ckeditor import CKEditor
# from flask_admin import Admin
from config import config

db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)

from . import db_models

def create_app(config_name):
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)

    from .main import main
    from .travlio_admin import shef

    app.register_blueprint(main, url_prefix='/')
    app.register_blueprint(shef, url_prefix='/admin')


    return app

# admins = Admin(app, name='Travlio', template_mode='bootstrap3')