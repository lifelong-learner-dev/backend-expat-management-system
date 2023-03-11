from django.contrib import admin
from .models import Work_permit

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