from django.db import models

class Portal_client(models.Model):
    name=models.CharField(max_length=200)
    adress=models.CharField(max_length=200)
    nif_stat=models.CharField(max_length=200)
    def __str__ (self):
        return self.name
class Type_add(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Add_portal(models.Model):
    name=models.CharField(max_length=200)
    type=models.ForeignKey(Type_add,on_delete=models.DO_NOTHING,related_name='add_type')
    portal_client=models.ForeignKey(Portal_client,on_delete=models.DO_NOTHING,related_name='add_client')
    # eto asiana sary
    def __str__(self):
        return self.name