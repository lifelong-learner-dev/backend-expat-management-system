from django.contrib import admin
from .models import House_rent_extension

@admin.register(House_rent_extension)
class House_rent_extensionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "responsible_person",
        "house",
        "new_rent_fee",
        "currency_new_rent",
        "limit",
        "currency_limit",
        "krstatus",
        "enstatus",
    )
    list_filter = (
        "name",
    )
    search_fields = (
        "name",
    )