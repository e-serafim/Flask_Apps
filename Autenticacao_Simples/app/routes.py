from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required

from app import db
from app.models import User
from app.auth import auth as auth_blueprint

def init_app(app):
    app.register_blueprint(auth_blueprint)

    @app.route("/")
    @login_required
    def index():
        users = User.query.all() # SELECT * FROM users
        return render_template('index.html', users=users)


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

    