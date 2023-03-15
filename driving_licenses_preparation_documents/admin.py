from django.contrib import admin
from .models import Driving_licenses_preparation_document

@admin.register(Driving_licenses_preparation_document)
class Driving_licenses_preparation_documentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "expat",
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
