from django.contrib import admin
from .models import Family_residence_permit

@admin.register(Family_residence_permit)
class Family_residence_permitAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "expat",
        "family",
        "first_name",
        "last_name",
        "turkish_id",
        "tc_id_expiry_date",
        "passport_number",
        "passport_expiry_date",
        "first_visit_date",
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