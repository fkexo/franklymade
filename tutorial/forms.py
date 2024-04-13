from django import forms
from django.db.models import fields
from django.forms import TextInput, Textarea
from crispy_forms.helper import FormHelper
from .models import PythonCourse, Course






class TinyMCEWidget(Textarea):
    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}
        attrs['class'] = 'tinymce'
        super().__init__(attrs=attrs)

class MyForm(forms.Form):
    description= forms.CharField(widget=TinyMCEWidget)



class CourseForm(forms.ModelForm):
    class Meta:
        model = Course

        fields = ('title','slug', 'description')


class PostCourseForm(forms.ModelForm):
    

    class Meta:
        model = PythonCourse
        # select the field we need in the create form

        fields = ('title', 'slug', 'description')
       
