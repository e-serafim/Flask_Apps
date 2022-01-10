from enum import unique
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(84), nullable=False, unique=True)

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

    return redirect(url_for('index'))

@app.route("/user/delete/<int:id>")
def delete(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)