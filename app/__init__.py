from flask import Flask 
from .config import Config
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

def create_app(): 
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    db.init_app(app)
    from app.routes.main import main_bp
    from app.routes.game import game_bp
    from app.routes.auth import auth_bp    
    app.register_blueprint(main_bp)
    app.register_blueprint(game_bp)
    app.register_blueprint(auth_bp)
    return app 