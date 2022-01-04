from django.urls import path
from . import views
app_name='applicant_cv'
urlpatterns = [
    path('',views.index, name='index')
]