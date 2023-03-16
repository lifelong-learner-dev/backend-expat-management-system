from django.contrib import admin
from .models import Company_cars_request, Explanation, Document

@admin.register(Company_cars_request)
class Company_cars_requestAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "expat",
        "accident_location",
        "accident_type",
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