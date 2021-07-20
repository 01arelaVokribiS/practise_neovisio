from django.contrib import admin
from .models import Client

# Only display all fields in admin page in all tables
class ClientAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'middlename', 'birth_date', 'telephone_number', 'address')


admin.site.register(Client, ClientAdmin)
