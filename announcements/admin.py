from django.contrib import admin
from .models import Announcement

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "subject",
        "start_date",
        "start_time",
        "finish_date",
        "finish_time",
        "created_at",
    )

    list_filter = (
        "name",
        "subject",
    )
    search_fields = (
        "name",
        "subject",
    )
