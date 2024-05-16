from django.db import models
from django.contrib.auth import get_user_model




User = get_user_model()



class BlogAuthor(models.Model):
    blog_author = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.author.username
    
class Category(models.Model):
    title = models.CharField(max_length=100)

class Article(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(null=True)
    body =  models.TextField(max_length=3000)
    postimage = models.FileField(blank=True, null=True)
    postdate = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    blog_author = models.ForeignKey(BlogAuthor, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title


    def shotend_body(self):
        return self.body[:200] + '...'
   
