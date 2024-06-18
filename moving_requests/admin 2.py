from django.contrib import admin
from .models import Moving_request

@admin.register(Moving_request)
class Moving_requestAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "expat",
        "arrival_location",
        "pre_survey_date",
        "pre_survey_time",
        "moving_start_date",
        "ensituation",
        "enstatus",
    )
    list_filter = (
        "name",
    )
    search_fields = (
        "name",
    )