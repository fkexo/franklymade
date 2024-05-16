from django.contrib import admin
from .models import News, NewsCategory
from django import forms









class NewsForm(forms.ModelForm):
    # content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = News
        fields = ['content',]


admin.site.register(News)
admin.site.register(NewsCategory)