from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interests = models.CharField(max_length=250, blank=True)
    profile_description = models.TextField(max_length=2500, blank=True)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class AcceptedCrypto(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=50, blank=True)
    code = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name


class ContactMethod(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=250, blank=True)
    url_link = models.URLField(blank=True)

    def __str__(self):
        return self.name
