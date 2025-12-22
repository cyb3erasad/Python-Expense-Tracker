from flask import Flask
from flask_login import LoginManager
from models import db
from routes import register_routes

def create_app():
    app =Flask(__name__)
    
    app.config["SECRET_KEY"] = "030603337850"
    app.config["SQLALCHEMY_DATABASE_URI"] = ("mysql+pymysql://root:asad2006db@localhost/expense_tracker")
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
