from django.shortcuts import render
from .models import AddProject
from django.core.mail import send_mail





def portinfo_home(request):
    
    return render(request, 'portinfo/portinfo_home.html')
    

def allProjects(request):
    all_project = AddProject.objects.all()
    context = {'all_project':all_project}
    return render(request, 'portinfo/allprojects.html', context)

def projectDetails(request):
    
    return render(request, 'portinfo/projectdetails.html')
    

    

