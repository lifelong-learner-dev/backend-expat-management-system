from django.contrib import admin
from .models import Green_cards_preparation_document

@admin.register(Green_cards_preparation_document)
class Green_cards_preparation_documentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "expat",
    )
    list_filter = (
        "name",
    )
    search_fields = (
        "name",
    )