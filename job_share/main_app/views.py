from django.shortcuts import render
from proposal_job_management.models import Job_proposal
from formation_management.models import Formation_proposal

# Create your views here.
def index(request):
    job_urgent=Job_proposal.objects.filter(urgent=True).order_by('-create_date')[:6]
    latest_formations= Formation_proposal.objects.order_by('-date_create')[:6]
    context={
        'job_urgent':job_urgent,
        'latest_formations':latest_formations,
    }
    return render(request,'main_app/index.html',context)

