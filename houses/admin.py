from django.contrib import admin
from .models import House

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