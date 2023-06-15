from django.contrib import admin
from .models import Driving_license

@admin.register(Driving_license)
class Driving_licenseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "expat",
        "family",
        "expat_have_driving_license",
        "spouse_have_driving_license",
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
