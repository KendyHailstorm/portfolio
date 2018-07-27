from django.shortcuts import render
from .models import Job

# Creating views to be viewed at home.

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html',{'jobs':jobs})
