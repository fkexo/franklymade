from django.contrib import admin
from .models import Lesson, CourseSeries, Category, Tag, Author


from ckeditor.widgets import CKEditorWidget
from django.db import models








class LessonFormAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }


admin.site.register(Author)
admin.site.register(CourseSeries)
admin.site.register(Lesson, LessonFormAdmin)
admin.site.register(Category)
admin.site.register(Tag)




