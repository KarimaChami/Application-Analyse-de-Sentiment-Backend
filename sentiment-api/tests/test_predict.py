
from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.main import app

client = TestClient(app)

# --- Fake user credentials ---
USERNAME = "kima"
PASSWORD = "password123"

# @pytest.fixture
# def token():
#     # Obtenir un token JWT
#     response = client.post("/login", json={"username": USERNAME, "password": PASSWORD})
#     assert response.status_code == 200
#     return response.json()["access_token"]


def test_login_success():
    response = client.post("/login", json={"username": USERNAME, "password": PASSWORD})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"