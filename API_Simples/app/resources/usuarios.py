from flask_restful import Resource
from app.models import User
from app import db
from flask import request
from werkzeug.security import check_password_hash, generate_password_hash

class Usuarios(Resource):
    def get(self):
        query = User.query.all()
        result = []
        for x in query:
            result.append(x.__str__())
        return {'usuarios': result}

    def post(self):
        user=User()
        user.name = request.values['name']
        user.email = request.values['email']
        user.password = generate_password_hash(request.values['pwd'])

        db.session.add(user)
        db.session.commit()

        return {'usuario cadastrado': user.__str__()}

    def put(self):
        nome=request.values['name']
        user = User.query.filter_by(name=nome).first()
        
        if not user:
            return {'message': 'Usuario não encontrado'}

        if not check_password_hash(user.password, request.values['pwd_antigo']):
            return {'message': 'Senha antiga incorreta'}

        user.password = generate_password_hash(request.values['pwd_novo'])

        db.session.add(user)
        db.session.commit()
        
        return {'Senha alterada': True}

    def delete(self):
        nome=request.values['name']
        user = User.query.filter_by(name=nome).first()

        if not user:
            return {'message': 'Usuario não encontrado'}

        db.session.delete(user)
        db.session.commit()

        return {'usuario deletado': nome}