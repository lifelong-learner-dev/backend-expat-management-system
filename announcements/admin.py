from django.contrib import admin
from .models import Announcement

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "subject",
        "start_date",
        "start_time",
        "finish_date",
        "finish_time",
        "created_at",
    )

    list_filter = (
        "title",
        "subject",
    )
    search_fields = (
        "title",
        "subject",
    )
