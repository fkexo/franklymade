from django.db import models
# from django.contrib.auth import get_user_model






# User = get_user_model()



class PythonCourse(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True)
    pupdate = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=3000, blank=True, null=True)
    
    
    
    def __str__(self):
        return self.title



class CourseCategory(models.Model):
    title = models.CharField(max_length=100)


    def __str__(self):
        return self.title



class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True)
    pup_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=3000, blank=True, null=True)
    

    def __str__(self):
        return self.title
    