Green Academy API - Secure Learning Platform

📌 Project Description

Green Academy provides an online learning platform for environmental sustainability. This API enables course management, user authentication, and enrollment functionality with enhanced security measures, including JWT authentication, role-based access control (RBAC), input validation, caching, and automated API documentation.

🚀 Setup Instructions

1️⃣ Clone the Repository

To get started, clone the repository and navigate into the project folder:

git clone <repo_link>
cd green_academy

2️⃣ Create a Virtual Environment & Install Dependencies

Set up a virtual environment to isolate dependencies:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

3️⃣ Configure Environment Variables

Create a .env file in the root directory and add the required secrets:

DJANGO_SECRET_KEY=your-secure-secret-key
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,summative-green-academy-api-final-phase.onrender.com
DATABASE_URL=your-database-url

4️⃣ Run Migrations & Start the Server

Apply database migrations and start the development server:

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

The API will be available at:

http://127.0.0.1:8000/

🛡️ Security Features

JWT Authentication: Users must obtain and pass a JWT token for API access.

Role-Based Access Control (RBAC): Admin, Instructor, and Student roles with specific permissions.

Secure Password Hashing: Uses Django’s built-in hashing mechanisms.

CORS Handling: Enables safe cross-origin requests from frontend applications.

Input Validation: Prevents SQL injection & XSS attacks using Django serializers.

Logging & Error Handling: Logs critical errors and prevents exposing sensitive data.

HTTPS Configuration (Production Ready): Enforces secure API communication.

🔗 API Endpoints

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

📌 Example API Request: User Registration

{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "securepassword123"
}

📌 Example API Response

{
  "message": "User registered successfully",
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com"
  }
}

📚 Courses Management

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

PUT

Update a course (Admin, Instructor)

/api/courses/{id}/

DELETE

Delete a course (Admin)

📋 Enrollments

Endpoint

Method

Description

/api/enrollments/

GET

View all enrollments

/api/enrollments/enroll/

POST

Enroll a student in a course

/api/enrollments/{id}/

DELETE

Withdraw from a course

/api/enrollments/my-courses/

GET

View enrolled courses

📚 API Documentation

Swagger Documentation is available at:

http://127.0.0.1:8000/swagger/

🚀 Deployment Guide

1️⃣ Deployment Platform Selection

We chose Render because it provides:

Free tier hosting for small projects

Automatic deployment from GitHub

Easy database configuration

Built-in HTTPS support

2️⃣ Deployment Steps

Push code to GitHub.

Link your GitHub repository to Render.

Set environment variables in Render:

DJANGO_SECRET_KEY

DEBUG=False

DATABASE_URL

Deploy the app using Gunicorn as the WSGI server.

Run database migrations:

python manage.py migrate

The API is now live at:

https://summative-green-academy-api-final-phase.onrender.com/

📀 Caching Strategy

Frequently accessed course data is cached using Redis with a 5-minute expiration.

🤖 Running Tests

Run the Django test suite to ensure all API endpoints work as expected:

python manage.py test

📜 Changelog

✅ Version 1.0 - Initial Release

Implemented user authentication with JWT

Added CRUD functionality for courses

Developed enrollment system with role-based permissions

Implemented caching with Redis

Integrated Swagger API documentation

📄 Known Limitations

No support for file uploads (future feature)

Only supports PostgreSQL for production deployment

Rate limiting is not yet implemented for authentication requests

🎉 Happy Coding!

