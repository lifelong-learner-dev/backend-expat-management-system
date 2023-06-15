from django.contrib import admin
from .models import Family_residence_permits_request

@admin.register(Family_residence_permits_request)
class Family_residence_permits_requestAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "expat",
        "residence_permits",
        "location",
        "date",
        "krstatus",
        "enstatus",
        "created_at",
    )

    list_filter = (
        "name",
        "expat",
        "residence_permits",
    )
    search_fields = (
        "name",
        "expat",
        "residence_permits",
    )

