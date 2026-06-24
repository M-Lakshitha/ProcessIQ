from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_generate_workflow() -> None:
    response = client.post("/workflows", json={"goal": "Build House", "state_code": "TN"})
    assert response.status_code == 200
    body = response.json()
    assert body["goal_detected"] == "Build House"
    assert body["prompt_hash"]
    assert "goal" not in body


def test_generate_land_sale_workflow() -> None:
    response = client.post("/workflows", json={"goal": "sale land", "state_code": "TN"})
    assert response.status_code == 200
    body = response.json()
    assert body["goal_detected"] == "Sale Land"
    assert body["phases"][1]["services"][0]["id"] == "sale-deed-registration"


def test_unsupported_state_message() -> None:
    response = client.post("/workflows", json={"goal": "Build House", "state_code": "KA"})
    assert response.status_code == 200
    assert "currently supports" in response.json()["message"]
