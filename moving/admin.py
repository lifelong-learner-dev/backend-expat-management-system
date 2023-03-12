from django.contrib import admin
from .models import Moving, Explanation

@admin.register(Moving)
class MovingAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "total_explanations",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "name",
    )
    search_fields = (
        "name",
    )

@admin.register(Explanation)
class ExplanationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "detailed_information",
        "created_at",
    )
    list_filter = (
        "name",
        "description",
    )
    search_fields = (
        "name",
        "description",
    )