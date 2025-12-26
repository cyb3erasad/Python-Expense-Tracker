from flask import render_template, redirect, flash, request, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import date
from models import db, User, Transaction
from sqlalchemy import extract


def register_routes(app, login_manager):
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    @app.route("/")
    def home():
        return render_template("home.html")
    
    @app.route("/register", methods=["GET", "POST"])
    def register():
        if request.method == "POST":
            username = request.form["username"]
            email = request.form["email"]
            password = request.form["password"]

            if User.query.filter_by(username=username).first():
                flash("Username already exist!", "danger")
                return redirect(url_for("register"))
            
            if User.query.filter_by(email=email).first():
                flash("Email already exist!", "danger")
                return redirect(url_for("register"))
            
            user = User(
                username=username,
                email=email,
                password=generate_password_hash(password)
            )
            db.session.add(user)
            db.session.commit()

            flash("Account created Successfully. Please Login..", "success")
            return redirect(url_for("login"))    
        return render_template("register.html")
    
    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]

            user = User.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for("dashboard"))
            flash("Invalid email or password", "danger")
        return render_template("login.html")    
    
    @app.route("/logout")
    def logout():
        logout_user()
        return redirect(url_for("login"))
    
    @app.route("/dashboard")
    @login_required
    def dashboard():
        today = date.today()

        income = db.session.query(db.func.sum(Transaction.amount)).filter(
            Transaction.user_id == current_user.id,
            Transaction.type == "income",
            extract("month", Transaction.date) == today.month,
            extract("year", Transaction.date) == today.year
        ).scalar() or 0

        expense = db.session.query(db.func.sum(Transaction.amount)).filter(
            Transaction.user_id == current_user.id,
            Transaction.type == "expense",
            extract("month", Transaction.date) == today.month,
            extract("year", Transaction.date) == today.year
        ).scalar() or 0

        balance = income - expense

        monthly_income = []
        monthly_expense = []

        for month in range(1, 13):
            inc = db.session.query(db.func.sum(Transaction.amount)).filter(
                Transaction.user_id == current_user.id,
                Transaction.type == "income",
                extract("month", Transaction.date) == month,
                 extract("year", Transaction.date) == today.year
            ).scalar() or 0
            
            exp = db.session.query(db.func.sum(Transaction.amount)).filter(
                Transaction.user_id == current_user.id,
                Transaction.type == "expense",
                extract("month", Transaction.date) == month,
                extract("year", Transaction.date) == today.year
            ).scalar() or 0   

            monthly_income.append(inc)
            monthly_expense.append(exp)  

        return render_template("dashboard.html",
                               income=income,
                               expense=expense,
                               balance=balance,
                               monthly_income=monthly_income,
                               monthly_expense=monthly_expense)
    
    @app.route("/add", methods=["GET", "POST"])
    @login_required
    def add_transaction():
        if request.method == "POST":
            transaction = Transaction(
                amount = request.form["amount"],
                type = request.form["type"],
                description = request.form["description"],
                date = request.form["date"],
                user_id = current_user.id
            )

            db.session.add(transaction)
            db.session.commit()
            return redirect(url_for("dashboard"))
        return render_template("add_transaction.html")
    

    @app.route("/transactions")
    @login_required
    def transactions():
        transactions = Transaction.query.filter_by(
            user_id = current_user.id
        ).order_by(Transaction.date.desc()).all()

        return render_template("transactions.html", transactions=transactions)
    

    @app.route("/delete/<int:id>", methods=["POST"])
    @login_required
    def delete(id):
        transactions = Transaction.query.get_or_404(id)

        if transactions.user_id != current_user.id:
            flash("Unauthorized action", "danger")
            return redirect(url_for("dashboard"))
        
        db.session.delete(transactions)
        db.session.commit()
        return redirect(url_for("dashboard"))
    