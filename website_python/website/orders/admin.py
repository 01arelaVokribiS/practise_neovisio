from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'employee', 'course')


admin.site.register(Order, OrderAdmin)