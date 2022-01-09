from django.urls import path
from . import views

app_name='authentication'

urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('contact/',views.contact, name='contact'),
    path('', views.index, name='index')
]
