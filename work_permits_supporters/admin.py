from django.contrib import admin
from .models import Work_permits_supporter

@admin.register(Work_permits_supporter)
class Work_permits_supporterAdmin(admin.ModelAdmin):
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