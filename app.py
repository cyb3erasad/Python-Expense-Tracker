from flask import Flask
from flask_login import LoginManager
from models import db
from routes import register_routes
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app =Flask(__name__)
    
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default_secret_key")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("MYSQL_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = "login"
    login_manager.init_app(app)

    register_routes(app, login_manager)

    with app.app_context():
        db.create_all()

    return app
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)    
