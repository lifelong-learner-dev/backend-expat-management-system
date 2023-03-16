from django.contrib import admin
from .models import Family_residence_permit, Explanation, Document, Visit_place

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

@admin.register(Explanation)
class ExplanationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "detailed_information",
        "created_at",
    )
    list_filter = (
        "name",
        "description",
    )
    search_fields = (
        "name",
        "description",
    )

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "detailed_information",
        "created_at",
    )
    list_filter = (
        "name",
        "description",
    )
    search_fields = (
        "name",
        "description",
    )

@admin.register(Visit_place)
class Visit_placeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "detailed_information",
        "created_at",
    )
    list_filter = (
        "name",
        "description",
    )
    search_fields = (
        "name",
        "description",
    )