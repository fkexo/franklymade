from django.db import models






class AddProject(models.Model):
    title = models.CharField(max_length=300)
    body =  models.TextField(max_length=3000)
    postimage = models.FileField(blank=True, null=True)
    postdate = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=80)
    detail_link = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.title


    def shotend_body(self):
        return self.body[:200] + '...'
   