from datetime import datetime

from django.db import models
from django.utils import timezone
from authentication.models import User
# from django.forms import  ModelForm

# Create your models here.


class Sector_type(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    def __str__(self):
        return self.name

class Job_contract_type(models.Model):
    name=models.CharField(max_length=200,verbose_name='Designation')
    description=models.TextField(verbose_name='Desc')
    def __str__(self):
        return self.name

class Job_proposal(models.Model):
    def date_available(self):
        return self.filter(date_available__lte = timezone.now())

    
    job_title=models.CharField(max_length=200)
    job_ref=models.CharField(max_length=200)
    city_region=models.CharField(max_length=200,verbose_name='Ville / Region ')
    contract_type=models.ForeignKey(Job_contract_type,on_delete=models.DO_NOTHING)
    lib_contract=models.CharField(max_length=200,default=" " )
    sector_type=models.ForeignKey(Sector_type,on_delete=models.DO_NOTHING, null=True)
    create_date=models.DateTimeField()

    job_description=models.TextField(default="")
    profile_searched=models.TextField(default="")

    proposal_expired_date=models.DateTimeField()
    enterprise_name=models.CharField(max_length=200,default='')
    enterprise_activity=models.CharField(max_length=200,default='')
    email=models.EmailField(default="")

    urgent=models.BooleanField(default=False)
    def __str__(self):
        return self.job_title + ' '+self.job_ref
    
    


