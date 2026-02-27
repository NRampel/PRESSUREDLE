from flask import Flask 
from .config import Config
from flask_sqlalchemy import SQLAlchemy 
from flask_session import Session

db = SQLAlchemy()
sess = Session()

def create_app(): 
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    db.init_app(app)
    sess.init_app(app)
    from app.routes.main import main_bp
    from app.routes.game import game_bp
    from app.routes.auth import auth_bp    
    app.register_blueprint(main_bp)
    app.register_blueprint(game_bp)
    app.register_blueprint(auth_bp)
    return app 


with create_app().app_context():
    db.create_all()
    print("DB created")