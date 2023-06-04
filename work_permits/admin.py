from django.contrib import admin
from .models import Work_permit, Explanation

@admin.register(Work_permit)
class Work_permitAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "expat",
        "krstatus",
        "enstatus",
        "created_at",
    )

    list_filter = (
        "name",
        "expat",
    )
    search_fields = (
        "name",
        "expat",
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