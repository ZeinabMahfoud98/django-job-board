from audioop import reverse
from django.shortcuts import redirect, render
from .forms import ApplyForm,AddJobForm
from .models import Job
from django.core.paginator import Paginator
# Create your views here.

def job_list(request):
    job_list=Job.objects.all()
    paginator=Paginator(job_list,1)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={'jobs':page_obj}
    return render(request,'job/job_list.html',context)

def job_detail(request,slug):
    job=Job.objects.get(slug=slug)
    #job=get_object_or_404(Job,id)

    if request.method=="POST":
        print('ok1')
        form=ApplyForm(request.POST,request.FILES)
        print('zzzzzzzzzzzzzzzzzzzzzzz')
        print(form)
        print('zzzzzzzzzzzzzzzzzzzzzzz')
        if form.is_valid():
            print('ok2')
            print('zzzzzzzzzzzzzzzzzzzzzzz')
            myform=form.save(commit=False)##return object
            print(myform)
            print('zzzzzzzzzzzzzzzzzzzzzzz')
            myform.job=job
            print(myform) ##print name for Apply models => str functions
            print('zzzzzzzzzzzzzzzz')
            myform.save()
    else:
        form=ApplyForm()

    context={'job':job,'form':form}
    return render(request,'job/job_details.html',context)


def add_job(request):
    
    if request.method=='POST':
        form=AddJobForm(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.owner=request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form=AddJobForm()

    context={'form':form}
    return render(request,'job/add_job.html',context)