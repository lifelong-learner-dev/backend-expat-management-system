from django.contrib import admin
from .models import Green_cards_request, Available_country

@admin.register(Green_cards_request)
class Green_cards_requestAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "expat",
        "green_card_period",
        "green_card_car_insurance_period",
        "green_card_departure_date",
        "will_you_request_green_card",
        "will_you_request_overseas_car_insurance",
        "do_you_have_power_of_attorney",
    )
    list_filter = (
        "name",
    )
    search_fields = (
        "name",
    )
@admin.register(Available_country)
class Available_countryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
    )
    list_filter = (
        "name",
    )
    search_fields = (
        "name",
    )