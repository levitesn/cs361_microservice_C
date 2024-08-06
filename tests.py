from fastapi.testclient import TestClient
from app import app
client = TestClient(app)


def test_create_trip():
    response = client.post("/trips", json={"destination": "Tokyo", "start_date": "2024-09-01", "end_date": "2024-09-10",
                                           "description": "Vacation in Tokyo"})
    assert response.status_code == 200
    assert response.json()["destination"] == "Tokyo"


def test_list_trips():
    response = client.get("/trips")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_trip():
    resp = client.post("/trips",
                json={"destination": "Berlin", "start_date": "2024-10-01", "end_date": "2024-10-10",
                      "description": "Vacation in Berlin"})
    trip_id = resp.json()["id"]

    response = client.get(f"/trips/{trip_id}")
    assert response.status_code == 200
    assert response.json()["destination"] == "Berlin"


def test_update_trip():
    resp = client.post("/trips",
                json={"destination": "Rome", "start_date": "2024-11-01", "end_date": "2024-11-10",
                      "description": "Vacation in Rome"})
    trip_id = resp.json()["id"]

    response = client.put(f"/trips/{trip_id}",
                          json={"destination": "Venice", "start_date": "2024-11-05", "end_date": "2024-11-15",
                                "description": "Updated vacation in Venice"})

    assert response.status_code == 200
    assert response.json()["destination"] == "Venice"


def test_delete_trip():
    resp = client.post("/trips",
                json={"destination": "Madrid", "start_date": "2024-12-01", "end_date": "2024-12-10",
                      "description": "Vacation in Madrid"})

    trip_id = resp.json()["id"]

    response = client.delete(f"/trips/{trip_id}")
    assert response.status_code == 200
    assert response.json()["destination"] == "Madrid"
