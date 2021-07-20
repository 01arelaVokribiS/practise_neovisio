from django.contrib import admin
from .models import Employee

# Only display all fields in admin page in all tables
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'middlename', 'position')

admin.site.register(Employee, EmployeeAdmin)