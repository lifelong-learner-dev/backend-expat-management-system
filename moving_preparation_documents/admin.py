from django.contrib import admin
from .models import Moving_preparation_document

@admin.register(Moving_preparation_document)
class Moving_preparation_documentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "expat",
        "ensituation",
    )
    list_filter = (
        "name",
    )
    search_fields = (
        "name",
    )