from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, BlogAuthor
from .forms import ArticleForm
from django.urls import reverse
from django.contrib import messages


def get_blog_author(user):
    queryset = BlogAuthor.objects.filter(blog_author = user)
    if queryset.exists():
        return queryset[0]
    return None

def blogHome(request):
    article_list = Article.objects.all()
    
    context = {
        'article_list':article_list,
        'messages':messages.get_messages(request)
               }
    return render(request, 'blog/bloghome.html', context)





def viewBlog(request, slug):
    article_list = get_object_or_404(Article, slug=slug)
    
    context = {'article_list':article_list}
    return render(request, 'blog/viewBlog.html', context)


def addArticle(request):
    
    
    if request.user.is_authenticated:
        author = get_blog_author(request.user)
        article_form = ArticleForm(request.POST or None, request.FILES or None)
        if request.method == 'POST':
            if article_form.is_valid():
                article_form.instance.author = author
                article_form.save()
                return redirect(reverse('article', kwargs={
                    'slug':article_form.instance.slug
                }))
                
            else:
                messages.error(request, 'something went wrong check your form')
                return redirect('add_article')


    # article_form = ArticleForm()
    context={'form':article_form}
    return render(request, 'blog/add_article.html', context)
    


