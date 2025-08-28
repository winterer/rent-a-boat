from fastapi.testclient import TestClient

from rentaboat.main import app

client = TestClient(app)


def test_read_boats_with_search():
    response = client.get("/boats?q=Yacht")
    assert response.status_code == 200
    boats = response.json()
    assert len(boats) == 1
    assert boats[0]["name"] == "Yacht"
    assert boats[0]["type"] == "sailing"


def test_read_boats_with_search_no_results():
    response = client.get("/boats?q=nonexistent")
    assert response.status_code == 200
    boats = response.json()
    assert len(boats) == 0


def test_read_boats_without_search():
    response = client.get("/boats")
    assert response.status_code == 200
    boats = response.json()
    assert len(boats) == 2
