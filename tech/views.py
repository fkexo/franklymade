from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import News
from .forms import TechNewsForm





def index(request):
    return render(request, 'tech/index.html')



def techHome(request):

    news_list = News.objects.all()
    context = {'news_list':news_list}
    return render(request, 'tech/tech_home.html', context)


def detailPage(request, slug):

    news = get_object_or_404(News, slug=slug)

    context = {"news_detail": news}
    
    return render(request, 'tech/detailpage.html', context)


def addTechNews(request):

    if request.user.is_authenticated:
        add_tech_news_form = TechNewsForm(request.POST or None, request.FILES or None)
        if request.method == "POST":
            add_tech_news_form.save()
            return redirect(reverse("course", kwargs={
                'slug':add_tech_news_form.instance.slug
            }))

    add_tech_news_form = TechNewsForm()
    context = {'form':add_tech_news_form}
    
    return render(request, 'tech/add_tech_news.html', context)