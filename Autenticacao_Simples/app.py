from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login.utils import logout_user
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
import os

from sqlalchemy.orm import backref

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = "secret"

db = SQLAlchemy(app)
login_manager = LoginManager(app)

@login_manager.user_loader
def current_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(84), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True, index=True)
    password = db.Column(db.String(255), nullable=False)

    def __str__(self):
        return self.name
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
        check = request.form['lembrar']

        user =  User.query.filter_by(email=email).first()
        if not user:
            flash('Usuário não encontrado!', 'danger')
            return render_template('login.html')

        if not check_password_hash(user.password, senha):
            flash('Senha incorreta!', 'danger')
            return render_template('login.html')

        login_user(user, remember=True if check=="on" else False, duration=timedelta(days=30))
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

@login_manager.unauthorized_handler
def unauthorized_callback():
    flash('Você tem que estar logado!', 'danger')
    return redirect(url_for('login'))

if __name__ == "__main__":
    if not os.path.exists('./app.db'):
        db.create_all()
    app.run(debug=True)