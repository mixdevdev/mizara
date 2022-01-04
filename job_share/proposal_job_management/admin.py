from django.contrib import admin
from .models import Job_proposal,Job_contract_type, Sector_type

# Register your models here.
@admin.register(Job_proposal)
class Job_proposal_admin(admin.ModelAdmin):
    pass


@admin.register(Sector_type)
class Sector_type_admin(admin.ModelAdmin):
    pass


@admin.register(Job_contract_type)
class Job_contract_type_admin(admin.ModelAdmin):
    pass

# @admin.register(Formation_proposal)
# class Formation_proposal_admin(admin.ModelAdmin):
#     pass

