from datetime import timedelta
import os

from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user, login_manager
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from app.models import User


def init_app(app):
    @app.route("/")
    @login_required
    def index():
        users = User.query.all() # SELECT * FROM users
        
        return render_template('index.html', users=users)

    @app.route("/register", methods=["GET", "POST"])
    def register():
        if request.method == "POST":
            user=User()
            user.name = request.form['name']
            user.email = request.form['email']
            user.password = generate_password_hash(request.form['pwd'])

            db.session.add(user)
            db.session.commit()

            flash('Usuário cadastrado com suceso!', 'success')

            return redirect(url_for('login'))

        return render_template('register.html')

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            email = request.form['email']
            senha = request.form['pwd']
            if 'lembrar' in request.form:
                remember=True
            else:
                remember=False

            user =  User.query.filter_by(email=email).first()
            if not user:
                flash('Usuário não encontrado!', 'danger')
                return render_template('login.html')

            if not check_password_hash(user.password, senha):
                flash('Senha incorreta!', 'danger')
                return render_template('login.html')

            login_user(user, remember=remember, duration=timedelta(days=30))
            return redirect(url_for('index'))

        return render_template('login.html')

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('login'))

    @app.route("/user/info/<int:id>")
    @login_required
    def info(id):
        user = User.query.filter_by(id=id).first()

        return render_template('user.html', user=user)

    @app.route("/user/delete/<int:id>")
    @login_required
    def delete(id):
        user = User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()

        flash('Usuário deletado com suceso!', 'danger')

        return redirect(url_for('index'))

    