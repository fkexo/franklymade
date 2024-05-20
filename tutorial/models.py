from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.shortcuts import redirect



    

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

    
class CourseSeries(models.Model):
    image = models.ImageField(upload_to='profile_pics/', default='default.jpg')

    course_title = models.CharField(max_length=200)
    description = models.TextField(default='description')
    date_created = models.DateField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, related_name='course_series_tags')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='course_series_category', default=1)
    featured_course = models.BooleanField(default=True)

    def __str__(self):
        return self.course_title
    
    def get_absolute_url(self):
        return reverse('course_detail', kwargs={"id":self.id})

    def short_description_text(self):
        return self.description[:100]+ "..."
    

    
class Lesson(models.Model):
    category = models.ForeignKey(Category, related_name='lessons', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True)
    pup_date = models.DateTimeField(auto_now_add=True)
    lesson_content = models.TextField(blank=True, null=True)
    lesson_count = models.IntegerField(default=0)
    featured_lesson = models.BooleanField(default=True)

    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    course_series = models.ForeignKey(CourseSeries, on_delete=models.CASCADE, related_name='lessons', blank=True, null=True)

    next_lesson = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='next_in_sequence')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        if self.next_lesson:
            return reverse('lesson', args=[str(self.next_lesson.slug)])
        else:
            # return reverse('course_detail', args=[str(self.course.id)]) 
            return reverse('lesson', args=[str(self.slug)])
    
    # def get_absolute_url(self):
    # return reverse('lesson', kwargs={'args': self.slug})
    
    def get_lesson_category(self):
        return self.category.cat_name
    
    def get_shortened_lesson_content(self):
        return self.lesson_content[:56] + "..."
    
    
    class Meta:
        ordering = ['pup_date']


