from django.contrib import admin
from .models import PythonCourse
from tinymce.widgets import TinyMCE
from django.db import models


from django.forms import ModelForm
from django.contrib.admin import ModelAdmin
from trumbowyg.widgets import TrumbowygWidget



# admin.site.register(PythonCourseAdmin)

#from django.forms import forms, Textarea
from tinymce.widgets import TinyMCE

formfield_overrides = {
  models.TextField: {'widget': TinyMCE()}
  }
admin.site.register(PythonCourse)
