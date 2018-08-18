from django.db import models
from django.contrib.auth.models import User

action_map = (
    ('GET', 'retrieve'),
    ('POST', 'create'),
    ('PUT', 'update'),
    ('PATCH', 'partial update'),
    ('DELETE', 'destroy'),
)
class Permission(models.Model):
    view = models.CharField(max_length=128)
    action = models.CharField(max_length=16,choices=action_map)

    def __str__(self):
        return self.view+' '+self.action

class Group(models.Model):
    permissions = models.ManyToManyField(Permission, related_name="permissions")
    user = models.ManyToManyField(User, related_name="consist")