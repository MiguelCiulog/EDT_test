from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_correct_response():
    latitude = 100.00
    longitude = 100.00
    radius = 63780000  # Max radius

    response = client.get(
        f"/v1/restaurants/statistics?latitude={latitude}&longitude={longitude}&radius={radius}"
    )
    assert response.status_code == 200
    assert isinstance(response.json()["count"], int)
    assert isinstance(response.json()["avg"], float)
    assert isinstance(response.json()["std"], float)


def test_no_response():
    # No restaurant found
    latitude = 0.0
    longitude = 0.0
    radius = 0.0

    response = client.get(
        f"/v1/restaurants/statistics?latitude={latitude}&longitude={longitude}&radius={radius}"
    )
    assert response.status_code == 404
    assert response.json() == {
        "detail": f"No restaurants found on radius: {radius}, latitude: {latitude}, longitude: {longitude}"
    }


def test_too_few_responses():
    # One restaurant exact location
    latitude = 19.4400570537131
    longitude = -99.1270470974249
    radius = 0.0

    response = client.get(
        f"/v1/restaurants/statistics?latitude={latitude}&longitude={longitude}&radius={radius}"
    )
    assert response.status_code == 422
    assert response.json() == {
        "detail": f"Only 1 restaurant found on radius: {radius}, latitude: {latitude}, longitude: {longitude}"
    }
