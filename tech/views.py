from django.shortcuts import render, get_object_or_404, redirect 
from django.urls import reverse

from .models import News, NewsCategory
from .forms import TechNewsForm

from tutorial.models import Lesson, CourseSeries

def index(request):
    news_list = News.objects.all()
    featured_news = News.objects.order_by("-pup_date")[:3]
    
    # Using .first() for safe querying in case no records exist
    recent_lesson = Lesson.objects.order_by('-pk').first()
    featured_lesson = Lesson.objects.order_by('pk').first()  # Changed to .first() for consistency
    recent_course_series = CourseSeries.objects.order_by('-pk').first()
    news_category = NewsCategory.objects.all()

    # Default message if no recent course series found
    if recent_course_series is None:
        recent_course_series = "No recent course found"
    
    featured_posts = News.objects.filter(featured_post=True)

    context = {
        'news_category':news_category,
        "recent_course_series": recent_course_series,
        'news_list': news_list,
        'featured_news': featured_news,
        'featured_lesson': featured_lesson,
        "featured_posts": featured_posts,
        "recent_lesson": recent_lesson
    }

    return render(request, 'tech/tech_home.html', context)


def techHome(request):
    news_list = News.objects.all()
    featured_news = News.objects.order_by("-pup_date")[:3]
    featured_lesson = Lesson.objects.order_by('pk').first()  # Use .first() for safety
    news_category = NewsCategory.objects.all()
    context = {
        'news_list': news_list,
        'featured_news': featured_news,
        'featured_lesson': featured_lesson,
        'news_category':news_category
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
    else:
        return redirect('tech_home')
    # For GET requests or non-authenticated users, show the form
    add_tech_news_form = TechNewsForm()
    context = {'form': add_tech_news_form}
    
    return render(request, 'tech/add_tech_news.html', context)




# def news_categories(request):
#     news_cat = NewsCategory.objects.all()

#     context= {'news_cat':news_cat}
#     return render(request, 'tech/news_category.html', context)


# def news_cat_item_list(request, news_cat_id):
#     news_cat_items = get_object_or_404(NewsCategory, id=news_cat_id)
    
#     context = {'news_cat_items':news_cat_items}
#     return render(request, 'category_item.html', context)


def news_category_list(request):
    categories = NewsCategory.objects.all()
    return render(request, 'tech/news_category_list.html', {'categories': categories})

# View to display news items by category
def news_by_category(request, category_slug):
    category = get_object_or_404(NewsCategory, slug=category_slug)
    news_items = News.objects.filter(news_category=category).order_by('-pup_date')  # Fetch by category and order by publication date
    news_category = NewsCategory.objects.all()

    return render(request, 'tech/category_item.html', {'news_items': news_items, 'category': category, "news_category":news_category})

# View for a specific news article
# def news_detail(request, slug):
#     news_item = get_object_or_404(News, slug=slug)
#     return render(request, 'tech/news_detail.html', {'news_item': news_item})
