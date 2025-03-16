from rest_framework import generics, permissions
from rest_framework.response import Response
from django.core.cache import cache
from .models import Course
from .serializers import CourseSerializer
from .permissions import IsStudent, IsInstructor, IsAdmin

class CourseListCreateView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        """
        Only instructors can create new courses.
        Only admins can edit existing courses.
        Everyone can read courses.
        """
        if self.request.method == "POST":
            # Only 'admin' users can create
            return [IsInstructor()]
        
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsAdmin()]

        return [permissions.AllowAny()]

    def list(self, request, *args, **kwargs):
        """
        Override list() to demonstrate caching. If performance is critical,
        consider DRF built-in caching or other patterns.
        """
        cached_courses = cache.get('courses')
        if cached_courses is None:
            courses = Course.objects.all()
            cache.set('courses', courses, timeout=60*5)
        else:
            courses = cached_courses

        serializer = self.get_serializer(courses, many=True)
        return Response({"status": "success", "data": serializer.data})

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # Adjust permissions as needed (admin/instructor can update/delete, etc.)
