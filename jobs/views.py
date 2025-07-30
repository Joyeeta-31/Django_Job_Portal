from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Job, Application
from .forms import JobForm, ApplicationForm

@login_required
def post_job(request):
    if request.user.role != 'employer':
        return redirect('dashboard')
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            return redirect('my_jobs')
    else:
        form = JobForm()
    return render(request, 'jobs/post_job.html', {'form': form})

@login_required
def my_jobs(request):
    if request.user.role != 'employer':
        return redirect('dashboard')
    jobs = Job.objects.filter(posted_by=request.user)
    return render(request, 'jobs/my_jobs.html', {'jobs': jobs})

@login_required
def applicants_list(request, job_id):
    job = get_object_or_404(Job, id=job_id, posted_by=request.user)
    applications = Application.objects.filter(job=job)
    return render(request, 'jobs/applicants_list.html', {'job': job, 'applications': applications})



@login_required
def job_list(request):
    if request.user.role != 'applicant':
        return redirect('dashboard')
    
    query = request.GET.get('q')
    jobs = Job.objects.all()
    if query:
        jobs = jobs.filter(
            Q(title__icontains=query) |
            Q(company_name__icontains=query) |
            Q(location__icontains=query)
        )

    return render(request, 'jobs/job_list.html', {'jobs': jobs})

@login_required
def job_detail(request, job_id):
    if request.user.role != 'applicant':
        return redirect('dashboard')
    
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            return redirect('my_applications')
    else:
        form = ApplicationForm()
    return render(request, 'jobs/job_detail.html', {'job': job, 'form': form})

@login_required
def my_applications(request):
    if request.user.role != 'applicant':
        return redirect('dashboard')
    
    applications = Application.objects.filter(applicant=request.user)
    return render(request, 'jobs/my_applications.html', {'applications': applications})

@login_required
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, posted_by=request.user)
    job.delete()
    return redirect('my_jobs')

