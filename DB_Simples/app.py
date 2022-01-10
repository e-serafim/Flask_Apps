from enum import unique
from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

from sqlalchemy.orm import backref

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = "secret"

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(84), nullable=False, unique=True)
    pokemons = db.relationship('Pokemon', backref='user')

    def __str__(self):
        return self.name

class Pokemon(db.Model):
    __tablename__ = "pokemons"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(84), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __str__(self):
        return self.name

@app.route("/")
def index():
    if not os.path.exists('./app.db'):
        return redirect(url_for('cria_db'))
    users = User.query.all() # SELECT * FROM users
    
    return render_template('index.html', users=users)

@app.route("/cria-db")
def cria_db():
    db.create_all()
    
    flash('app.db criado com sucesso!', 'success')

    return redirect(url_for('index'))

@app.route("/user/info/<int:id>")
def info(id):
    user = User.query.filter_by(id=id).first()

    return render_template('user.html', user=user)


@app.route("/user/add/<name>")
def add(name):
    user=User()
    user.name=name
    db.session.add(user)
    db.session.commit()

    flash('usuário adicionado com sucesso!', 'success')

    return redirect(url_for('index'))

@app.route("/pokemon/add/<name_user>-<name_pokemon>")
def add_pokemon(name_user, name_pokemon):
    user = User.query.filter_by(name=name_user).first()
    if user:
        pokemon=Pokemon()
        pokemon.name=name_pokemon
        pokemon.user_id=user.id
        db.session.add(pokemon)
        db.session.commit()

        flash('pokemon adicionado com sucesso!', 'success')
    else:
        flash('Usuário não encontrado! Pokemon não adicionado!', 'danger')

    return redirect(url_for('index'))


@app.route("/user/delete/<int:id>")
def delete(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()

    flash('Usuário deletado com suceso!', 'danger')

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)