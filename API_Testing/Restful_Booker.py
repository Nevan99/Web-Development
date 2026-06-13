import requests
import pytest

BASE_URL = "https://restful-booker.herokuapp.com"

# --- Get Auth Token ---
@pytest.fixture(scope="session")
def auth_token():
    response = requests.post(f"{BASE_URL}/auth", json={
        "username": "admin",
        "password": "password123"
    })
    assert response.status_code == 200
    return response.json()["token"]

# --- Create Booking ---
@pytest.fixture(scope="session")
def booking_id(auth_token):
    payload = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {"checkin": "2025-01-01", "checkout": "2025-01-07"},
        "additionalneeds": "Breakfast"
    }
    response = requests.post(f"{BASE_URL}/booking", json=payload)
    assert response.status_code == 200
    return response.json()["bookingid"]

# --- Tests ---
def test_get_all_bookings():
    response = requests.get(f"{BASE_URL}/booking")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_booking_by_id(booking_id):
    response = requests.get(f"{BASE_URL}/booking/{booking_id}")
    assert response.status_code == 200
    assert response.json()["firstname"] == "John"

def test_update_booking(auth_token, booking_id):
    headers = {"Cookie": f"token={auth_token}"}
    payload = {
        "firstname": "Jane",
        "lastname": "Smith",
        "totalprice": 200,
        "depositpaid": False,
        "bookingdates": {"checkin": "2025-02-01", "checkout": "2025-02-07"},
        "additionalneeds": "Lunch"
    }
    response = requests.put(f"{BASE_URL}/booking/{booking_id}", json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json()["firstname"] == "Jane"

def test_partial_update(auth_token, booking_id):
    headers = {"Cookie": f"token={auth_token}"}
    response = requests.patch(
        f"{BASE_URL}/booking/{booking_id}",
        json={"firstname": "Updated"},
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()["firstname"] == "Updated"

def test_delete_booking(auth_token, booking_id):
    headers = {"Cookie": f"token={auth_token}"}
    response = requests.delete(f"{BASE_URL}/booking/{booking_id}", headers=headers)
    assert response.status_code == 201