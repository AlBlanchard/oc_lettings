from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "favorite_city")
    search_fields = ("user__username", "favorite_city")
