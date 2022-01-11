from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

from . import forms
# Create your views here.
def index(request):
    return render(request,'authentication/index.html')

def contact(request):
    return render(request,'authentication/contact.html')


def signup(request):
    if request.method == 'POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request,"Registration done")
            return redirect ("main_app:index")
        messages.error(request,"error ")
    form=NewUserForm()
    return render(request,'authentication/register.html',context={"register_form":form})

def signout(request):
    logout(request)
    return render(request,'main_app/index.html')

# def login(request):
#     form=forms.Login_user()
#     if request.method == 'POST':
#         if forms.Login_user(request.POST):
#             print('mandeha eto')
#             print(form)
#             if form.is_valid():
#                 print('here')
#                 user = authenticate(
#                     username=form.cleaned_data['username'],
#                     password=form.cleaned_data['password'],
#                 )
                
#                 if user is not None:
#                     login(request, user)
#                 # message = f'Bonjour, {user.username}! Vous êtes connecté.'
#             # else:
#             #     message = 'Identifiants invalides.'
#     return render(request,'authentication/login.html',context={'form':form})
