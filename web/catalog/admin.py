from django.contrib import admin

from .models import Address, Device

admin.site.register(Address)
admin.site.register(Device)
