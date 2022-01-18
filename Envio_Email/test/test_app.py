import pytest
from app import create_app, db
from app.models import User

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"
    app.config['WTF_CSRF_ENABLED'] = False

    context = app.app_context()
    context.push()

    db.create_all()

    yield app.test_client()

    db.session.remove()
    db.drop_all()

    context.pop()

def test_se_a_pagina_login_retorna_status_code_200(client):
    response = client.get("/login")
    assert response.status_code == 200

def test_se_o_link_de_register_existe(client):
    response = client.get("/login")
    assert "Register" in response.get_data(as_text=True)

def test_registrando_usuario(client):
    data = {
        'name': 'Zezinho',
        'email': 'Zezinho@teste.com',
        'pwd': '123'
    }
    response = client.post('/register', data=data, follow_redirects=True)
    assert "Usuário cadastrado com sucesso!" in response.get_data(as_text=True)

def test_register_e_logando_usuario(client):
    data = {
        'name': 'Zezinho',
        'email': 'Zezinho@teste.com',
        'pwd': '123'
    }
    client.post('/register', data=data, follow_redirects=True)
    response = client.post('/login', data=data, follow_redirects=True)
    assert "Sair" in response.get_data(as_text=True)

def test_register_e_errando_senha_no_login(client):
    data = {
        'name': 'Zezinho',
        'email': 'Zezinho@teste.com',
        'pwd': '123'
    }
    client.post('/register', data=data, follow_redirects=True)
    data['pwd']='1234'
    response = client.post('/login', data=data, follow_redirects=True)
    assert "Senha incorreta!" in response.get_data(as_text=True)