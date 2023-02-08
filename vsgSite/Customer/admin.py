from django.contrib import admin

from .models import Customer, License

admin.site.register(Customer)
admin.site.register(License)
