from django.contrib import admin
from .models import Work_permits_process

@admin.register(Work_permits_process)
class Work_permits_processAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "responsible_person",
        "created_at",
    )

    list_filter = (
        "title",
        "responsible_person",
    )
    search_fields = (
        "title",
        "responsible_person",
    )