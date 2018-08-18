from django.db import models
from django.contrib.auth.models import User

action_map = (
    ('retrieve','GET'),
    ('create','POST'),
    ('update','PUT'),
    ('partial_update','PATCH'),
    ('destroy','DELETE'),
)
class Permission(models.Model):
    view = models.CharField(max_length=128)
    action = models.SmallIntegerField(choices=action_map)

class Group(models.Model):
    permissions = models.ManyToManyField(Permission, related_name="permissions")
    user = models.ManyToManyField(User, related_name="consist")