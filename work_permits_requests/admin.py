from django.contrib import admin
from .models import Work_permits_request

@admin.register(Work_permits_request)
class Work_permits_requestAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "expat",
        "location",
        "date",
        "krstatus",
        "enstatus",
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