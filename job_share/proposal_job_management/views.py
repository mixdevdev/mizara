from django.shortcuts import render
from .forms import Job_proposal_forms
from .models import Job_proposal
# from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    form=Job_proposal_forms()
    print("test here")
    if request.method == 'POST':
        print(request.method)
        form=Job_proposal_forms(request.POST)
        if form.is_valid():
            print('valid ve')
            form.save()
        else:
            print('NOT VALID')
    context={'form':form}
    return render(request,'proposal_job_management/index.html',context)


def list_job(request):
    latest_job=Job_proposal.objects.order_by('-create_date')
    context={'latest_job':latest_job}
    return render(request,'proposal_job_management/list_jobs.html',context)
# Create your views here.
# def index(request):
#     return render(request,'proposal_job_management/index.html')

# def index(request):
#     form=Job_proposal_forms()
#     context={}
#     if request.method == 'POST':
#         print(request.method)
#         form=Job_proposal_forms(request.POST)
#         if form.is_valid():
#             form.save()
#         context={'form':form}
#     return render(request,'proposal_job_management/index.html',context)
