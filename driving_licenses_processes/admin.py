from django.contrib import admin
from .models import Driving_licenses_process

@admin.register(Driving_licenses_process)
class Driving_licenses_processAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "responsible_person",
        "created_at",
    )

    list_filter = (
        "name",
        "responsible_person",
    )
    search_fields = (
        "name",
        "responsible_person",
    )