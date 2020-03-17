from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=10000, blank=True)
    geolocation = models.CharField(max_length=150, blank=True)
    accepted_cryptos = models.ForeignKey("AcceptedCrypto", on_delete=models.CASCADE)


class AcceptedCrypto(models.Model):
    name = models.CharField(max_length=50, blank=True)
    code = models.CharField(max_length=10, blank=True)