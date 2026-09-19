import os
import sys


# Allow pytest to import app.py from the project root
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)


from app import app


def test_home_page():
    """Check that the UniGo home page loads successfully."""

    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"UniGo" in response.data


def test_journey_page():
    """Check that the journey page loads successfully."""

    client = app.test_client()

    response = client.get("/journey")

    assert response.status_code == 200
    assert b"MY JOURNEY" in response.data


def test_health_endpoint():
    """Check that the health endpoint reports a healthy application."""

    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["application"] == "UniGo"
    assert data["status"] == "healthy"