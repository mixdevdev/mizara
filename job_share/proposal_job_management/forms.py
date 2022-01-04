from django import forms
from django.forms import ModelForm

from .models import Job_proposal

# class Add_proposal(forms.Form):
#     job_title=forms.CharField(label='Title',max_length=100)
#     # job_ref=forms.CharField(label='Ref',max_length=100)
#     # city_region=forms.CharField(label='Ville / Région')
class Job_proposal_forms(ModelForm):
    class Meta:
        model=Job_proposal
        fields='__all__'
        widgets={
            'job_title':forms.TextInput(attrs={
                'class':'form-control testcss',
                'placeholder':"Job Title",
                'aria-label':"JobTitle",
            }),
            'job_ref':forms.TextInput(attrs={
                'class':'form-control testcss',
                'placeholder':"Job Ref",
                'aria-label':"JobRef",
            }),
            'city_region':forms.TextInput(attrs={
                'class':'form-control testcss',
                'placeholder':"City or Region",
                'aria-label':"cityRegion",
            }),
            'contract_type':forms.Select(attrs={
                'class':'form-select'
            }),
            'lib_contract':forms.Textarea(attrs={
                'class':'form-control',
                'aria-label':"cityRegion",
            }),
            'sector_type':forms.Select(attrs={
                'class':'form-select',
                'aria-label':"cityRegion",
            }),
            'job_description':forms.Textarea(attrs={
                'class':'form-control',
                'aria-label':"cityRegion",
            }),
            'profile_searched':forms.Textarea(attrs={
                'class':'form-control',
                'aria-label':"cityRegion",
            }),
            'enterprise_name':forms.TextInput(attrs={
                'class':'form-control',
                'aria-label':"cityRegion",
            }),
            'enterprise_activity':forms.TextInput(attrs={
                'class':'form-control',
                'aria-label':"cityRegion",
            }),
            'email':forms.TextInput(attrs={
                'class':'form-control',
                'aria-label':"cityRegion",
            }),
        }