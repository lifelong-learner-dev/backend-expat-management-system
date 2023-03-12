from django.contrib import admin
from .models import Green_card, Explanation

@admin.register(Green_card)
class Green_cardAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "expat",
        "green_card_expiry_date",
        "overseas_car_insurance_expiry_date",
        "total_explanations",
        "created_at",
        "updated_at",
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