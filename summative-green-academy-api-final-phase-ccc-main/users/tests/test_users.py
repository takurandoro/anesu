from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('user-register')
        self.token_url = reverse('token_obtain_pair')

    def test_user_registration(self):
        payload = {
            "username": "newuser",
            "password": "newpass123",
            "email": "newuser@example.com"
        }
        response = self.client.post(self.register_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_token_obtain(self):
        # Create a user first
        user = User.objects.create_user(
            username="loginuser", password="loginpass123", email="login@example.com"
        )
        payload = {
            "username": "loginuser",
            "password": "loginpass123"
        }
        response = self.client.post(self.token_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
