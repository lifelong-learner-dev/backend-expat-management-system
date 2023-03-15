from django.contrib import admin
from .models import Family_residence_permits_request, Explanation, Document

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