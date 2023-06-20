from django.contrib import admin
from .models import Additional_information_supporter

@admin.register(Additional_information_supporter)
class Additional_information_supporterAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "responsible_person",
        "created_at",
    )

    list_filter = (
        "name",
        "responsible_person",
    )
    search_fields = (
        "name",
        "responsible_person",
    )