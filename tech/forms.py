from django import forms
from django.db.models import fields
from django.forms import Textarea, TextInput
from crispy_forms.helper import FormHelper
from crispy_forms.helper import FormHelper
from .models import News



class TinyMCEWidget(Textarea):
    def __init__(self, attrs=None):
        if attrs is None:
            attrs ={}
        attrs['class']='tinymce'
        super().__init__(attrs=attrs)


class MyForm(forms.Form):
    content = forms.CharField(widget=TinyMCEWidget)


class TechNewsForm(forms.ModelForm):
    class Meta:
        model = News

        fields = ("title", 'content', 'slug', 'news_category', "news_source")
        # fields = ('image', "title", 'content', 'slug', 'news_category', "news_source")





