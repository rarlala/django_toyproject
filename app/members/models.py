from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    send_email = models.BooleanField(default=True)
    authorization = models.BooleanField(default=False)
