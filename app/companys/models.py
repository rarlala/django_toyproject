from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=20)
    address = models.TextField()

class Info(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    desc = models.TextField()
    price = models.CharField(max_length=20)
    soldout = models.BooleanField(default=True)
