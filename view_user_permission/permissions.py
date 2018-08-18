from rest_framework import permissions
from .models import Permission

class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.roles.filter(permissions__view=view.__class__.__name__,
                                        permissions__action=view.action).exists()
