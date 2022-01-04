from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.

class User(AbstractUser):
    is_employee=models.BooleanField(default=False)
    is_trainer=models.BooleanField(default=False)
    is_user=models.BooleanField(default=True)

    enterprise_name=models.CharField(max_length=200)


