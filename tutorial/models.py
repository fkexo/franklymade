from django.db import models
from django.contrib.auth import get_user_model




    

class PythonCourse(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True)
    pupdate = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title

class MainCourse(models.Model):
    course_title = models.CharField(max_length=200)
    description = models.TextField(default='description')

    def __str__(self):
        return self.course_title

# IIIIIIIIIIIII(this is what is in use)IIIIIIIIIIIIIIIIIIIII

User = get_user_model()

class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='media', default='franklymade/images/avataaars_5.png/')

    def __str__(self):
        return self.author.username

class Tag(models.Model):
    tag_name = models.CharField(max_length=100, default='add_tag')

    def __str__(self):
        return self.tag_name
    
class Category(models.Model):
    cat_name = models.CharField(max_length=100)

    def __str__(self):
        return self.cat_name

class Lesson(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True)
    pup_date = models.DateTimeField(auto_now_add=True)
    lesson_content = models.TextField(blank=True, null=True)
    lesson_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
    
class CourseSeries(models.Model):
    course_title = models.CharField(max_length=200)
    description = models.TextField(default='description')
    date_created = models.DateField(auto_now_add=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_title
    

