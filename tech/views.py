from django.shortcuts import render, get_object_or_404, redirect 
from django.urls import reverse

from .models import News
from .forms import TechNewsForm

from tutorial.models import Lesson, CourseSeries

def index(request):
    news_list = News.objects.all()
    featured_news = News.objects.order_by("-pup_date")[:3]
    
    # Using .first() for safe querying in case no records exist
    recent_lesson = Lesson.objects.order_by('-pk').first()
    featured_lesson = Lesson.objects.order_by('pk').first()  # Changed to .first() for consistency
    recent_course_series = CourseSeries.objects.order_by('-pk').first()

    # Default message if no recent course series found
    if recent_course_series is None:
        recent_course_series = "No recent course found"
    
    featured_posts = News.objects.filter(featured_post=True)

    context = {
        "recent_course_series": recent_course_series,
        'news_list': news_list,
        'featured_news': featured_news,
        'featured_lesson': featured_lesson,
        "featured_posts": featured_posts,
        "recent_lesson": recent_lesson
    }

    return render(request, 'tech/index.html', context)


def techHome(request):
    news_list = News.objects.all()
    featured_news = News.objects.order_by("-pup_date")[:3]
    featured_lesson = Lesson.objects.order_by('pk').first()  # Use .first() for safety

    context = {
        'news_list': news_list,
        'featured_news': featured_news,
        'featured_lesson': featured_lesson
    }

    return render(request, 'tech/tech_home.html', context)


def detailPage(request, slug):
    featured_news = News.objects.order_by("-pup_date")[:3]
    featured_lesson = Lesson.objects.order_by('pk').first()  # Use .first()

    # Fetch the specific news item by slug, or return 404 if not found
    news = get_object_or_404(News, slug=slug)

    context = {
        "news_detail": news,
        "featured_news": featured_news,
        'featured_lesson': featured_lesson  # Fixed the extra space issue
    }
    
    return render(request, 'tech/detailpage.html', context)


def addTechNews(request):
    if request.user.is_authenticated:
        add_tech_news_form = TechNewsForm(request.POST or None, request.FILES or None)
        if request.method == "POST" and add_tech_news_form.is_valid():
            add_tech_news_form.save()
            return redirect(reverse("course", kwargs={
                'slug': add_tech_news_form.instance.slug
            }))

    # For GET requests or non-authenticated users, show the form
    add_tech_news_form = TechNewsForm()
    context = {'form': add_tech_news_form}
    
    return render(request, 'tech/add_tech_news.html', context)
