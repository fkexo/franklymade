from django import forms
from django.forms import TextInput, Textarea
from crispy_forms.helper import FormHelper
from django.db.models import fields
from .models import Article




class MyForm(forms.Form):
    # description= forms.CharField(widget=TinyMCEWidget)
    pass



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article

        fields = ('title', 'category', 'slug', 'body')

