from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class SecurityTests(APITestCase):
    def test_sql_injection_protection(self):
        url = reverse('course-list-create')
        # Attempt to break SQL
        data = {
            "title": "'; DROP TABLE courses; --", 
            "description": "Hacking attempt",
            "duration": "1 week"
        }
        response = self.client.post(url, data)
        # Expecting validation or error — generally 400
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)

    def test_xss_protection(self):
        url = reverse('course-list-create')
        data = {
            "title": "<script>alert('Hacked!')</script>",
            "description": "XSS attack",
            "duration": "1 week"
        }
        response = self.client.post(url, data)
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)
