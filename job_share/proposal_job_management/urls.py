from django.urls import path
from . import views

app_name='proposal_job_management'

urlpatterns = [
    path('', views.index, name='index'),
    path('job_list/',views.list_job, name='list_job')
    # path('job_content/<int:job_id>',views.job_content,name='job_content')
]
