from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()

class IntegrationTests(APITestCase):
    def setUp(self):
        """
        Create a staff user so we can pass IsAdminUser (which checks is_staff).
        We do NOT use client.login() because we're relying on JWT auth.
        """
        self.staff_user = User.objects.create_user(
            username="adminuser",
            password="adminpass",
            email="admin@example.com",
            is_staff=True  # Crucial for IsAdminUser
        )

    def test_course_creation_and_retrieval(self):
        """
        Obtain a JWT token for the staff user, then create and list courses.
        Expect:
          - POST to /api/courses/ => 201 CREATED (because user is admin/staff)
          - GET to /api/courses/  => 200 OK
        """
        # 1) Obtain JWT token for the staff user
        token_response = self.client.post(
            '/api/users/token/',
            {
                "username": "adminuser",
                "password": "adminpass"
            },
            format="json"
        )
        self.assertEqual(token_response.status_code, status.HTTP_200_OK, "Failed to obtain JWT token")
        access_token = token_response.data["access"]

        # 2) Set the Authorization header to use the JWT
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')

        # 3) Attempt to create a course
        course_data = {
            "title": "Sustainable Energy",
            "description": "Learn about clean energy sources.",
            "duration": "4 weeks"
        }
        create_response = self.client.post("/api/courses/", course_data, format="json")
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED,
                         f"Expected 201 CREATED, got {create_response.status_code}")

        # 4) Retrieve list of courses
        list_response = self.client.get("/api/courses/")
        self.assertEqual(list_response.status_code, status.HTTP_200_OK,
                         f"Expected 200 OK, got {list_response.status_code}")

        # Assuming your CourseListCreateView returns {"status": ..., "data": [...]}
        self.assertIn("data", list_response.data, "Response should contain a 'data' key")
        self.assertEqual(len(list_response.data["data"]), 1, "Should have exactly 1 course in the list")
