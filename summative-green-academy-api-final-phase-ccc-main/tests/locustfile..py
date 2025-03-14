# locustfile.py (could be in tests/ or project root)
from locust import HttpUser, task, between

class CourseLoadTest(HttpUser):
    wait_time = between(1, 3)

    @task
    def load_courses(self):
        self.client.get("/api/courses/")
