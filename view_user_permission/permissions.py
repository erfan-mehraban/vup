from rest_framework import permissions
from .models import Permission

class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        print( request.user.role.filter(permissions__view=view.__class__.__name__, permissions__action=request.method).exists() )
        return True