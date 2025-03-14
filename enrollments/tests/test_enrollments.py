from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from users.models import User
from courses.models import Course
from enrollments.models import Enrollment

class EnrollmentTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.enroll_url = reverse('enroll-in-course')
        self.list_url = reverse('list-enrollments')

        self.user = User.objects.create_user(username="testuser", password="testpass", role="student")
        self.course = Course.objects.create(
            title="Chemistry 101",
            description="Intro to Chemistry",
            duration="10 weeks"
        )

    def test_enroll_in_course(self):
        """
        Test enrolling a user in a course.
        """
        self.client.force_authenticate(user=self.user)
        payload = {
            "student_id": self.user.id,
            "course_id": self.course.id
        }
        response = self.client.post(self.enroll_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Enrollment.objects.filter(student=self.user, course=self.course).exists())

    def test_list_enrollments(self):
        """
        Test listing all enrollments.
        """
        Enrollment.objects.create(student=self.user, course=self.course)
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Should have 1 enrollment
