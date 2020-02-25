from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=20)
    address = models.TextField()
