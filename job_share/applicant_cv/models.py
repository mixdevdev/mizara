from django.db import models
from authentication.models import  User
# Create your models here.

class Degree(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Curriculum(models.Model):
    name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    profile_photo=models.ImageField()
    birth_date=models.DateTimeField()
    # nationality=models.IntegerField
    path_linkedin=models.CharField(max_length=200)
    degree=models.ForeignKey(Degree,on_delete=models.DO_NOTHING,related_name='curriculum_degree')
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='curriculum_user')
    def __str__(self):
        return self.name