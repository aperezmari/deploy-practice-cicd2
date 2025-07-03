import pytest
from app import app, multiplicar, es_par

# ---------- Fixtures -----------------------------------------------
@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

# ---------- Tests de rutas -----------------------------------------
def test_home(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Hola" in resp.data

def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "healthy"}

def test_suma(client):
    resp = client.get("/suma/3/4")
    assert resp.status_code == 200
    assert resp.get_json() == {"resultado": 7}

def test_saludo(client):
    resp = client.get("/saludo/allen")
    assert resp.status_code == 200
    assert resp.data.decode() == "Hola, Allen!"

# ---------- Tests de funciones internas ----------------------------
@pytest.mark.parametrize("a,b,esperado", [(2, 5, 10), (7, 0, 0)])
def test_multiplicar(a, b, esperado):
    assert multiplicar(a, b) == esperado

@pytest.mark.parametrize("n,esperado", [(2, True), (3, False)])
def test_es_par(n, esperado):
    assert es_par(n) is esperado
