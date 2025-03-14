from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    duration = models.CharField(max_length=20)

    def __str__(self):
        return self.title
