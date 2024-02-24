from django.contrib import admin

# Register your models here.

from .models import FreeLesson, Courses

admin.site.register(FreeLesson)

admin.site.register(Courses)