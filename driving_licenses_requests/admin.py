from django.contrib import admin
from .models import Driving_licenses_request

@admin.register(Driving_licenses_request)
class Driving_licenses_requestAdmin(admin.ModelAdmin):
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
