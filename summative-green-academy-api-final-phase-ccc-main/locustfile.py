from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://127.0.0.1:8000"  # ✅ Set the correct base URL for the API

    @task
    def test_course_list(self):
        self.client.get("/api/courses/")
