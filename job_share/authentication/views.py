from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


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
