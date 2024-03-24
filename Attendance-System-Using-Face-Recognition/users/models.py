# models.py

from django.db import models
from django.contrib.auth.models import User

import datetime

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class_column = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

class Present(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    present = models.BooleanField(default=False)
    class_name = models.CharField(max_length=255)

class Time(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    time = models.DateTimeField(null=True, blank=True)
    out = models.BooleanField(default=False)
    class_name = models.CharField(max_length=255)
