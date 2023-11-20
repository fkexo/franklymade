from django.db import models



class Article(models.Model):
    title = models.CharField(max_length=300)
    body =  models.TextField(max_length=3000)
    postimage = models.FileField(blank=True, null=True)
    postdate = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title


    def shotend_body(self):
        return self.body[:200] + '...'
   
