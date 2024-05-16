from django import forms
from django.db.models import fields
from django.forms import TextInput, Textarea
from crispy_forms.helper import FormHelper
from .models import PythonCourse, Lesson





# class MyForm(forms.Form):
#     description= forms.CharField(widget=TinyMCEWidget)



# class LessonForm(forms.ModelForm):
#     class Meta:
#         model = Lesson

#         fields = ('title', 'slug', 'lesson_category', 'course', 'lesson_content')


# class PostCourseForm(forms.ModelForm):
    

#     class Meta:
#         model = PythonCourse
#         # select the field we need in the create form

#         fields = ('title', 'slug', 'description')
       
