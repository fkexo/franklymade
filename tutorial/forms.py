from django import forms
from django.db.models import fields
from django.forms import TextInput
from crispy_forms.helper import FormHelper


from .models import PythonCourse








class PostCourseForm(forms.ModelForm):
    

    class Meta:
        model = PythonCourse
        # select the field we need in the create form

        fields = ('title', 'description')
       
