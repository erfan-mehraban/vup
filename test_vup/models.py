from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Number(models.Model):
    value = models.IntegerField()

class User(AbstractUser):
    roles = models.ManyToManyField('view_user_permission.Group', related_name="users")