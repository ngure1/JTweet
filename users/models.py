from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class CustomUserModel(AbstractUser):
    phoneNumber=models.IntegerField(null=True, blank=True)
    dateCreated=models.DateTimeField(default = datetime.now)