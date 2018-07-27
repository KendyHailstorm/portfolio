from django.shortcuts import render

# Creating views to be viewed at home.

def home(request):
    return render(request, 'jobs/home.html')
