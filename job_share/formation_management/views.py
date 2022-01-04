from django.shortcuts import render
from .models import Formation_proposal

# Create your views here.

def index(request):
    all_formations=Formation_proposal.objects.order_by('-date_create')
    context={
        'all_informations':all_formations
    }
    return render(request,'formation_management/index.html',context)