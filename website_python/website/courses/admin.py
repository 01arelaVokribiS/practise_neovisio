from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'available', 'category')


admin.site.register(Course, CourseAdmin)