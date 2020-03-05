from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=20)
    address = models.TextField()

class Info(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    desc = models.TextField()
    price = models.CharField(max_length=20, null=True)
    soldout = models.BooleanField(default=True)

# test를 위한 models 생성
class Mask_Info(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()
    price = models.CharField(max_length=20, null=True)
    soldout = models.BooleanField(default=True)