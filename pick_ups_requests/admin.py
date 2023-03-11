from django.contrib import admin
from .models import Pick_ups_request

@admin.register(Pick_ups_request)
class Pick_ups_requestAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "expat",
        "location",
        "date",
        "time",
        "driver",
        "vehicle",
    )
    list_filter = (
        "name",
    )
    search_fields = (
        "name",
    )