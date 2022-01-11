from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name='authentication'

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('signout/',views.signout,name='signout'),
    path('login/', LoginView.as_view(
            template_name='authentication/login.html',
            redirect_authenticated_user=True),
        name='login'),
    # path('login/',views.login,name='login'),
    path('contact/',views.contact, name='contact'),
    path('', views.index, name='index')
]
