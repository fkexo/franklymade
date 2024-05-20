from django.contrib import admin
from .models import News, NewsCategory
from django import forms


from ckeditor.widgets import CKEditorWidget
from django.db import models





class NewsFormAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }


class NewsForm(forms.ModelForm):
    # content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = News
        fields = ['content',]


admin.site.register(News, NewsFormAdmin)
admin.site.register(NewsCategory)