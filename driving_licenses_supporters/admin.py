from django.contrib import admin
from .models import Driving_licenses_supporter

@admin.register(Driving_licenses_supporter)
class Driving_licenses_supporterAdmin(admin.ModelAdmin):
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