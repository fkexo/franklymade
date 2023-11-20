from django.db import models

class PythonCourse(models.Model):
    title = models.CharField(max_length=200)
    pupdate = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=3000, blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title