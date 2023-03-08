from django.contrib import admin
from .models import Process, Explanation, Document

@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "responsible_person",
        "total_explanations",
        "total_documents",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "name",
    )
    search_fields = (
        "name",
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