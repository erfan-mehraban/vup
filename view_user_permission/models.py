from django.db import models
from cityhash import CityHash32
from django.conf import settings

class Permission(models.Model):
    action_map = (
        (0,'retrieve'),
        (1,'list'),
        (2,'create'),
        (3,'update'),
        (4,'partial_update'),
        (5,'destroy'),
    )
    name = models.IntegerField(primary_key=True, default=0)
    view = models.CharField(max_length=128)
    action = models.PositiveSmallIntegerField(choices=action_map)

    def save(self, *args, **kwargs):
        self.name = self.get_name(self.view, self.action)
        super().save(*args, **kwargs)
    
    @staticmethod
    def get_name(view, action):
        if action is None:
            action = ""
        return CityHash32(view+action)

    def __str__(self):
        return self.view+' '+self.get_action_display()


class Group(models.Model):
    name = models.CharField(max_length=64, default="NO_NAME")
    permissions = models.ManyToManyField(Permission, related_name="groups")
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="roles")

    def __str__(self):
        return self.name
