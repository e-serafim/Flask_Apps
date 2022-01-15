from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required

from app import db
from . import user
from app.models import User

@user.route("/")
@login_required
def index():
    users = User.query.all() # SELECT * FROM users
    return render_template('index.html', users=users)


@user.route("/user/info/<int:id>")
@login_required
def info(id):
    user = User.query.filter_by(id=id).first()

    return render_template('user.html', user=user)

@user.route("/user/delete/<int:id>")
@login_required
def delete(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()

    flash('Usuário deletado com suceso!', 'danger')

    return redirect(url_for('user.index'))