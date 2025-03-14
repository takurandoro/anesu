🌱 Green Academy API - API Design

📌 Overview

The Green Academy API enables secure course management, user authentication, and student enrollments. This document outlines the API structure, including endpoints, authentication, roles, data models, and security considerations.

1️⃣ API Architecture

Framework: Django REST Framework (DRF)

Authentication: JWT Authentication (via djangorestframework-simplejwt)

Authorization: Role-Based Access Control (RBAC)

Database: PostgreSQL (deployed) / SQLite (local)

Caching: Redis (for optimized data retrieval)

Documentation: Swagger (auto-generated API documentation)

2️⃣ Authentication & User Management

All API requests require authentication using JWT tokens.A user must first log in to receive a JWT token, which must be included in Authorization Headers:

Authorization: Bearer <JWT_TOKEN>

User Roles

Role

Description

Permissions

Admin

Manages all users, courses, and enrollments.

Full access.

Instructor

Can create and manage courses.

Create, update, delete own courses.

Student

Can enroll in courses.

View and enroll in courses.

3️⃣ API Endpoints

🔑 Authentication & User Management

Endpoint

Method

Description

/api/users/register/

POST

Register a new user

/api/users/token/

POST

Obtain JWT token (Login)

/api/users/token/refresh/

POST

Refresh JWT token

/api/users/profile/

GET

Retrieve logged-in user profile

📚 Course Management

Endpoint

Method

Description

/api/courses/

GET

Retrieve all courses

/api/courses/

POST

Create a new course (Admin, Instructor)

/api/courses/{id}/

GET

Retrieve a single course

/api/courses/{id}/

PUT

Update a course (Admin, Instructor)

/api/courses/{id}/

DELETE

Delete a course (Admin)

📝 Enrollment Management

Endpoint

Method

Description

/api/enrollments/

GET

Retrieve all enrollments (Admin)

/api/enrollments/enroll/

POST

Enroll a student in a course

/api/enrollments/my-courses/

GET

View enrolled courses (Student)

/api/enrollments/{id}/

DELETE

Withdraw from a course (Student)

🔍 API Documentation

Swagger UI is available at:

http://127.0.0.1:8000/swagger/

4️⃣ Data Models

User Model

class User(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('instructor', 'Instructor'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=20, choices=ROLES, default='student')

Course Model

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'instructor'})
    created_at = models.DateTimeField(auto_now_add=True)

Enrollment Model

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

5️⃣ Security Features

✅ Authentication & Authorization

Uses JWT authentication.

RBAC ensures only authorized users can access endpoints.

✅ Data Validation

All input data is validated using serializers to prevent SQL Injection & XSS.

✅ Rate Limiting

API rate limiting is enforced to prevent abuse:

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_RATES': {
        'user': '1000/day',
    }
}

✅ CORS & CSRF Protection

CORS is configured to restrict requests to trusted origins:

CORS_ALLOWED_ORIGINS = ['http://localhost:3000', 'https://yourfrontend.com']

6️⃣ Performance Optimizations

✅ Database Indexing

Indexes added to improve query performance:

class Course(models.Model):
    title = models.CharField(max_length=255, db_index=True)  # Indexed field

✅ Caching with Redis

Frequently accessed course data is cached to reduce database load:

from django.core.cache import cache

def get_cached_courses():
    cached_courses = cache.get('courses')
    if cached_courses is None:
        cached_courses = list(Course.objects.all())
        cache.set('courses', cached_courses, timeout=60*5)
    return cached_courses

✅ Pagination for Large Responses

API responses are paginated to improve performance:

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

7️⃣ Error Handling

✅ Custom Error Responses

def custom_error_response(exception, context):
    response = exception_handler(exception, context)
    if response is None:
        return Response({"error": "An unexpected error occurred."}, status=500)
    return response

✅ Common Error Responses

Status Code

Meaning

Possible Causes

400

Bad Request

Invalid input data

401

Unauthorized

Missing or invalid JWT token

403

Forbidden

User lacks permissions

404

Not Found

Requested resource does not exist

500

Server Error

Unexpected backend issue

8️⃣ API Documentation & Testing

✅ Swagger UI

Interactive API docs at /swagger/

Automatically generated OpenAPI schema.

✅ Unit & Integration Testing

Test coverage includes:

Authentication & Role-Based Access

Input validation & security testing

Performance testing with Locust

Run all tests with:

python manage.py test

