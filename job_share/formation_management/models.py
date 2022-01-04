from django.db import models
from django.utils import timezone
from authentication.models import User


# Create your models here.
class Formation_proposal(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    location=models.CharField(max_length=200)
    teacher=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='formation_user')
    enterprise=models.CharField(max_length=200)
    date_create=models.DateField()
    def __str__(self):
        return self.name
        