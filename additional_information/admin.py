from django.contrib import admin
from .models import Additional_information

@admin.register(Additional_information)
class Additional_informationAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "subtitle",
        "contents",
        "detailed_information",
        "subtitle2",
        "contents2",
        "detailed_information2",
        "subtitle3",
        "contents3",
        "detailed_information3",
        "subtitle4",
        "contents4",
        "detailed_information4",
        "subtitle5",
        "contents5",
        "detailed_information5",
        "subtitle6",
        "contents6",
        "detailed_information6",
        "subtitle7",
        "contents7",
        "detailed_information7",
        "subtitle8",
        "contents8",
        "detailed_information8",
        "subtitle9",
        "contents9",
        "detailed_information9",
        "subtitle10",
        "contents10",
        "detailed_information10",
        "created_at",
    )



    list_filter = (
        "title",
        "subtitle",
    )
    search_fields = (
        "title",
        "subtitle",
    )
