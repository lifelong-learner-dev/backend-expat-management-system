from django.contrib import admin
from .models import Green_cards_process

@admin.register(Green_cards_process)
class Green_cards_processAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "responsible_person",
        "created_at",
    )

    list_filter = (
        "title",
        "responsible_person",
    )
    search_fields = (
        "title",
        "responsible_person",
    )