from django.contrib import admin
from .models import Moving

@admin.register(Moving)
class MovingAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "subtitle",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "title",
    )
    search_fields = (
        "title",
    )