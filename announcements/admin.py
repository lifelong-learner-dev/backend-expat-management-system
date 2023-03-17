from django.contrib import admin
from .models import Announcement, Explanation, Document, Visit_place

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

@admin.register(Explanation)
class ExplanationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "detailed_information",
        "created_at",
    )
    list_filter = (
        "name",
        "description",
    )
    search_fields = (
        "name",
        "description",
    )

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "detailed_information",
        "created_at",
    )
    list_filter = (
        "name",
        "description",
    )
    search_fields = (
        "name",
        "description",
    )

@admin.register(Visit_place)
class Visit_placeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "detailed_information",
        "created_at",
    )
    list_filter = (
        "name",
        "description",
    )
    search_fields = (
        "name",
        "description",
    )