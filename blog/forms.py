from django import forms
from django.forms import TextInput, Textarea
from crispy_forms.helper import FormHelper
from django.db.models import fields
from .models import Article




class TinyMCEWidget(Textarea):
    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}
        attrs['class'] = 'tinymce'
        super().__init__(attrs=attrs)

class MyForm(forms.Form):
    description= forms.CharField(widget=TinyMCEWidget)



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article

        fields = ('title', 'category', 'slug', 'body')

