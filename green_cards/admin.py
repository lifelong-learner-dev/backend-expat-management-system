from django.contrib import admin
from .models import Green_card

@admin.register(Green_card)
class Green_cardAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "expat",
        "green_card_expiry_date",
        "overseas_car_insurance_expiry_date",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "name",
    )
    search_fields = (
        "name",
    )