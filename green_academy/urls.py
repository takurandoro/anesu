from django.contrib import admin
from django.urls import path, include
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.http import JsonResponse


def root_view(request):
    """Root endpoint just returns a simple JSON message."""
    return JsonResponse({
        "message": "Welcome to the Green Academy API",
        "api_endpoints": {
            "Courses (list/create)": "/api/courses/",
            "Courses (detail)": "/api/courses/<id>/",
            "Enroll in Course": "/api/enrollments/enroll/",
            "List Enrollments": "/api/enrollments/list/",
            "User Register": "/api/users/register/",
            "JWT Token": "/api/users/token/",
            "JWT Refresh": "/api/users/token/refresh/",
            "Swagger Docs": "/swagger/"
        }
    })


schema_view = get_schema_view(
    openapi.Info(
        title="Green Academy API",
        default_version='v1',
        description="API documentation for Green Academy",
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('', root_view, name='root'),
    path('admin/', admin.site.urls),
    path('api/courses/', include('courses.urls')),
    path('api/enrollments/', include('enrollments.urls')),
    path('api/users/', include('users.urls')),

    # Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
