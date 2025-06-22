from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_objects(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import bp as api_bp
    app.register_blueprints(api_bp)

    return app