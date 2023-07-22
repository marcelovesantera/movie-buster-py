from rest_framework import permissions
from rest_framework.views import Request, View
from users.models import User


class IsEmployeeOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True

        if request.user.is_authenticated and request.user.is_employee:
            return True

        return False


class HasToken(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

        return False


class IsEmployeeOrUserOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, user: User) -> bool:
        if request.user.is_employee or user.id == request.user.id:
            return True

        return False
