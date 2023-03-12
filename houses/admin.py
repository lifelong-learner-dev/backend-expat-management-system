from django.contrib import admin
from .models import House, Clause, Explanation, Regulation

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "current_rent_fee",
        "currency_rent",
        "limit",
        "currency_limit",
    )
    list_filter = (
        "name",
    )
    search_fields = (
        "name",
    )
@admin.register(Clause)
class ClauseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "krclause",
        "trclause",
        "created_at",
    )
    list_filter = (
        "name",
    )
    search_fields = (
        "name",
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

@admin.register(Regulation)
class RegulationAdmin(admin.ModelAdmin):
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