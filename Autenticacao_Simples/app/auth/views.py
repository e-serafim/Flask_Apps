from datetime import timedelta

from app import db
from app.models import User
from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from . import auth


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user=User()
        user.name = request.form['name']
        user.email = request.form['email']
        user.password = generate_password_hash(request.form['pwd'])

        db.session.add(user)
        db.session.commit()

        flash('Usuário cadastrado com suceso!', 'success')

        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth.route("/login", methods=["GET", "POST"])
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
        return redirect(url_for('user.index'))

    return render_template('login.html')

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
