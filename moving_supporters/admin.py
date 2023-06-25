from django.contrib import admin
from .models import Moving_supporter

@admin.register(Moving_supporter)
class Moving_supporterAdmin(admin.ModelAdmin):
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