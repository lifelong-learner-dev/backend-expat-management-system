from django.contrib import admin
from .models import Familyresidencepermit

@admin.register(Familyresidencepermit)
class FamilyresidencepermitAdmin(admin.ModelAdmin):
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