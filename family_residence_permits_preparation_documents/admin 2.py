from django.contrib import admin
from .models import Family_residence_permits_preparation_document

@admin.register(Family_residence_permits_preparation_document)
class Family_residence_permits_preparation_documentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "expat",
        "endocument",
    )
    list_filter = (
        "name",
    )
    search_fields = (
        "name",
    )