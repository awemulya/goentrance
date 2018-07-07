from django.contrib.auth.models import User
from django.db import models

from core.models import Course


class Package(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, related_name="packages", on_delete=models.CASCADE)


class Tokens(models.Model):
    token = models.CharField(max_length=100, unique=True)
    package = models.ForeignKey(Package, related_name="tokens", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="tokens", blank=True, null=True, on_delete=models.CASCADE)
    activated_date = models.DateTimeField(auto_now_add=True)
