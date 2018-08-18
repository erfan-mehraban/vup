from django.db import models
from django.contrib.auth.models import User

action_map = (
    ('GET', 'retrieve'),
    ('POST', 'create'),
    ('PUT', 'update'),
    ('PATCH', 'partial update'),
    ('DELETE', 'destroy'),
)

action_map_dictionary = dict(action_map)
class Permission(models.Model):
    view = models.CharField(max_length=128)
    action = models.CharField(max_length=16,choices=action_map)

    def __str__(self):
        return self.view+' '+action_map_dictionary[self.action]


class Group(models.Model):
    name = models.CharField(max_length=64, default="NO_NAME")
    permissions = models.ManyToManyField(Permission, related_name="groups")
    user = models.ManyToManyField(User, related_name="roles")

    def __str__(self):
        return self.name
