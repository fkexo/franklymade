from django.db import models








class NewsCategory(models.Model):
    title = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.title


class News(models.Model):
    image = models.ImageField(upload_to='profile_pics/', default='default.jpg')
    title = models.CharField(max_length=200)
    content = models.TextField(default='content')
    slug = models.SlugField()
    pup_date = models.DateTimeField(auto_now_add=True)
    news_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    news_source = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return self.title


    def shortened_news_content(self):
        return self.content[:100] + '...'
