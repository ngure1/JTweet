from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUserModel(AbstractUser):
    phoneNumber=models.IntegerField(null=True, blank=True)