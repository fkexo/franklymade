from django.shortcuts import render, redirect
from .models import AddProject
from django.core.mail import send_mail
from .forms import Contact_Me_Form
from django.contrib import messages





def portinfo_home(request):
    
    form = Contact_Me_Form()
    response = ""
    if form.is_valid():
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        phone = form.cleaned_data["phone"]
        message = form.cleaned_data["message"]

        subject = name
        message = message
        sender = email
        phone = phone

        recipients = ["frankmadu2live@gmail.com"]
        
        try:
            send_mail(f'{subject}', f'{message}', f'{sender}', ['frankmadu2live@gmail.com'])
            messages.success(request, f"Hello! {subject}, your message was sent successfully, we would reply you shortly")
            return redirect('portinfo')

            
        except:
            messages.success(request, f"{subject}, your message was not sent ")
            
            return redirect('portinfo')

       

    
    context = {'contact_me_form':form,}
    
    return render(request, 'portinfo/home.html', context)
    

def allProjects(request):
    all_project = AddProject.objects.all()
    context = {'all_project':all_project}
    return render(request, 'portinfo/allprojects.html', context)

def projectDetails(request):
    
    return render(request, 'portinfo/projectdetails.html')
    


