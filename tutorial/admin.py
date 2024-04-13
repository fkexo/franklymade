from django.contrib import admin
from .models import PythonCourse, Course, CourseCategory



# tynimce widget initialization


admin.site.register(Course)
admin.site.register(PythonCourse)

admin.site.register(CourseCategory)


