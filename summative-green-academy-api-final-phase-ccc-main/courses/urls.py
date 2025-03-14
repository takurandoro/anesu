from django.urls import path
from .views import CourseListCreateView, CourseDetailView

urlpatterns = [
    path('', CourseListCreateView.as_view(), name='course-list-create'),  # Name matches security tests
    path('<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
]
