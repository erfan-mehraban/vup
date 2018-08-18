from rest_framework import permissions
from .models import Permission

class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.roles.filter(
            permissions__name=Permission.get_name(view.__class__.__name__, view.action)
            ).exists()
