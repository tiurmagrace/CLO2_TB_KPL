from fastapi.testclient import TestClient
from event_api.main import app

client = TestClient(app)

def test_create_event():
    response = client.post("/events/", json={
        "title": "Seminar AI",
        "location": "Kampus A",
        "date": "2025-06-10",
        "participants": []
    })
    assert response.status_code == 201
    assert response.json()["title"] == "Seminar AI"

def test_list_events():
    response = client.get("/events/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
