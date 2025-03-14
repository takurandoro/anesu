from django.urls import path
from .views import EnrollInCourseView, GetEnrollmentsView

urlpatterns = [
    path('enroll/', EnrollInCourseView.as_view(), name='enroll-in-course'),
    path('list/', GetEnrollmentsView.as_view(), name='list-enrollments'),
]
