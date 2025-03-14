from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from users.models import User
from courses.models import Course

class CourseTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.course_list_url = reverse('course-list-create')  
        # Adjust if your URL name is different.

        # Create an admin user (with unique email & is_staff=True)
        self.admin_user = User.objects.create_user(
            username="admin",
            password="adminpass",
            email="admin@example.com",
            is_staff=True  # Needed for IsAdminUser permission
        )

        # Create a non-admin (student) user
        self.student_user = User.objects.create_user(
            username="student",
            password="studentpass",
            email="student@example.com",
            is_staff=False
        )

        # Create an existing course just so we can test listing
        self.course = Course.objects.create(
            title="Test Course",
            description="A sample course",
            duration="2 weeks"
        )

    def test_list_courses_unauthenticated(self):
        """
        Unauthenticated (and also non-admin) users can list courses 
        because `get_permissions()` only restricts POST for admins.
        """
        response = self.client.get(self.course_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('data', response.data, "Response should include a 'data' key for the course list.")

    def test_create_course_as_admin(self):
        """
        Admin user should be able to create a course (201 CREATED).
        """
        self.client.force_authenticate(user=self.admin_user)
        payload = {
            "title": "New Course",
            "description": "Admin-only creation",
            "duration": "4 weeks"
        }
        response = self.client.post(self.course_list_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Optionally, check the response data or confirm the course is in the DB

    def test_create_course_as_student_forbidden(self):
        """
        Student (non-admin) user should receive 403 FORBIDDEN when posting.
        """
        self.client.force_authenticate(user=self.student_user)
        payload = {
            "title": "Unauthorized Course",
            "description": "No admin rights",
            "duration": "4 weeks"
        }
        response = self.client.post(self.course_list_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
