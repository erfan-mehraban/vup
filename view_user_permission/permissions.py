from rest_framework import permissions
from .models import Permission
from . import register

class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if not hasattr(view, 'action'):
            return False
        return request.user.roles.filter(
            permissions__name=Permission.get_name(register.get_view_name(view.__class__), view.action)
            ).exists()
