from django.shortcuts import render, redirect
from .models import Article



def index(request):
    article_list = Article.objects.all()
    
    context = {'article_list':article_list}
    return render(request, 'blog/index.html', context)





def viewBlog(request, article_id):
    article_list = Article.objects.get(pk=article_id)
    
    context = {'article_list':article_list}
    return render(request, 'blog/viewBlog.html', context)


    



def services(request):
    #  myobject = modeltemp.objects.all()
    context = {}
    return render(request, 'blog/services.html', context)



def about_blog(request):
    context = {}
    return render(request, 'blog/about_blog.html', context)


def contact_me(request):
      
    if request.method == "POST":
        message_phone = request.POST['phone']
        message_name  = request.POST['name']
        message_email  = request.POST['email']
        messagebody = request.POST['message']
        
        



        send_mail(
            message_email,
            messagebody + ' \n client name: ' + message_name + ' \n client phone: ' + message_phone + ' \n client phone: ' + message_email,
            messagebody[0:0] + '...',
            ['inspiredburdsinfo@gmail.com']
            )
            

       



        return render(request, 'myapp/contactus.html', {'message_name':message_name})
    else:
        return render(request, 'myapp/contactus.html', {})
