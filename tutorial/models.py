from django.db import models
# from tinymce.models import HTMLField

class PythonCourse(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True)
    pupdate = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=3000, blank=True, null=True)
    # content = HTMLField(default='content')
    
    
    def __str__(self):
        return self.title