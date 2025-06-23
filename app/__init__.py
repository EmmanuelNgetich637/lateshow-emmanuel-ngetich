from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from .models import db


# ✅ Correctly instantiate here
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # ✅ Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import bp as api_bp
    app.register_blueprint(api_bp)  # ✅ No 's' here

    return app
