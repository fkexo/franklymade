from django.db import models
from django.urls import reverse







class NewsCategory(models.Model):
    title = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.title


class News(models.Model):
    image = models.ImageField(default='default.jpg')
    title = models.CharField(max_length=200)
    content = models.TextField(default='content')
    slug = models.SlugField()
    pup_date = models.DateTimeField(auto_now_add=True)
    news_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    news_source = models.CharField(max_length=200, blank=True, null=True)
    featured_post = models.BooleanField(default=False)

    def __str__(self):
        return self.title


    def shortened_news_content(self):
        return self.content[:100] + '...'

    def get_absolute_url(self):
        # return reverse('lesson', args=[str(self.slug)])
        return reverse('lesson', kwargs={"slug":self.slug})

    