from django.db import models
from django.urls import reverse

class NewsCategory(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class News(models.Model):
    news_image = models.ImageField(upload_to='media', default='None')
    title = models.CharField(max_length=200)
    content = models.TextField(default='content')
    slug = models.SlugField(unique=True)  # Ensuring slug is unique to avoid conflicts
    pup_date = models.DateTimeField(auto_now_add=True)
    news_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, related_name='news')
    news_source = models.CharField(max_length=200, blank=True, null=True)
    featured_post = models.BooleanField(default=False)
    external_link = models.CharField(max_length=500, default='source link', blank=True, null=True)


    def __str__(self):
        return f"{self.title} ({self.news_category.title})"

    def shortened_news_content(self):
        return self.content[:100] + '...'  # To display a short version of the content

    def get_absolute_url(self):
        return reverse('lesson', kwargs={"slug": self.slug})  # Ensure the URL name matches your URL patterns
