from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """Only admin users."""
    def has_permission(self, request, view):
        return (request.user.is_authenticated and 
                request.user.role == 'admin')

class IsInstructor(BasePermission):
    """Only users with role='instructor'."""
    def has_permission(self, request, view):
        return (request.user.is_authenticated and 
                request.user.role == 'instructor')

class IsStudent(BasePermission):
    """Only users with role='student'."""
    def has_permission(self, request, view):
        return (request.user.is_authenticated and 
                request.user.role == 'student')
