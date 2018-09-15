from rest_framework import permissions
from rest_framework.permissions import *
from .models import Permission
from .helper import get_view_name
from django.contrib.auth.models import AnonymousUser

class UserPermission(permissions.IsAuthenticated):

    def has_permission(self, request, view):
        # if user was not athenticated
        if not super().has_permission(request, view):
            return False
        if not hasattr(view, 'action'):
            return False
        return request.user.roles.filter(
            permissions__name=Permission.get_name(get_view_name(view.__class__), view.action)
            ).exists()
