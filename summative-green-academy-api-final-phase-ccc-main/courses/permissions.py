from rest_framework import permissions

class IsInstructorOrAdmin(permissions.BasePermission):
    """
    Custom permission: Only instructors or admins can create/update courses.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.is_staff or request.user.role == 'instructor')

class IsStudentOrReadOnly(permissions.BasePermission):
    """
    Custom permission: Students can only view courses, not modify them.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role != 'student'
