from django.contrib import admin
from .models import Letting, Address


@admin.register(Letting)
class LettingAdmin(admin.ModelAdmin):
    list_display = ("title", "address")
    search_fields = ("title", "address__city", "address__street")


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("number", "street", "city", "state", "zip_code")
    search_fields = ("street", "city", "state", "zip_code")
