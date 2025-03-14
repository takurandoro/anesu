from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import Enrollment
from users.models import User
from courses.models import Course
from .serializers import EnrollmentSerializer

class EnrollInCourseView(APIView):
    """
    POST:  { "student_id": <int>, "course_id": <int> }
    """
    def post(self, request):
        student_id = request.data.get('student_id')
        course_id = request.data.get('course_id')

        try:
            student = User.objects.get(id=student_id)
            course = Course.objects.get(id=course_id)
            enrollment, created = Enrollment.objects.get_or_create(student=student, course=course)

            if not created:
                return Response({"message": "Student is already enrolled in this course."}, 
                                status=status.HTTP_400_BAD_REQUEST)
            return Response({"message": "Enrollment successful!"}, status=status.HTTP_201_CREATED)

        except User.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

class GetEnrollmentsView(ListAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    # You can add permission classes here if needed (e.g., only instructors/admins can view).
