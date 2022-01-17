import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    context = app.app_context()
    context.push()

    yield app.test_client()

    context.pop()

def test_se_a_pagina_login_retorna_status_code_200(client):
    response = client.get("/login")
    assert response.status_code == 200