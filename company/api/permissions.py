from rest_framework import permissions


class IsStaff(permissions.BasePermission):
    """Если админ, можно изменять список сотрудников."""

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.is_staff is True
