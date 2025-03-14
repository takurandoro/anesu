import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def test_user(db):
    user = User.objects.create_user(username="testuser", password="testpass", role="student")
    return user

def test_jwt_authentication(api_client, test_user):
    response = api_client.post(
        '/api/users/token/',
        {"username": "testuser", "password": "testpass"},
        format="json"
    )
    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data
    assert "refresh" in response.data
