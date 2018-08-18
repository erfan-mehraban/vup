from django.db import models
from django.contrib.auth.models import User
from cityhash import CityHash32

action_map_list = ['retrieve', 'list', 'create', 'update', 'partial_update', 'destroy']
action_map = tuple([(x,x) for x in action_map_list])

action_map_dictionary = dict(action_map)
class Permission(models.Model):
    name = models.IntegerField(primary_key=True, default=0)
    view = models.CharField(max_length=128)
    action = models.CharField(max_length=16,choices=action_map)

    def save(self, *args, **kwargs):
        self.name = self.get_name(self.view, self.action)
        super().save(*args, **kwargs)
    
    @staticmethod
    def get_name(view, action):
        if action is None:
            action = ""
        return CityHash32(view+action)

    def __str__(self):
        return self.view+' '+action_map_dictionary[self.action]


class Group(models.Model):
    name = models.CharField(max_length=64, default="NO_NAME")
    permissions = models.ManyToManyField(Permission, related_name="groups")
    user = models.ManyToManyField(User, related_name="roles")

    def __str__(self):
        return self.name
