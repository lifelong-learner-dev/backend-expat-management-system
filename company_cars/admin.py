from django.contrib import admin
from .models import Company_car

@admin.register(Company_car)
class Company_carAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "responsible_person",
        "created_at",
    )

    list_filter = (
        "name",
        "responsible_person",
    )
    search_fields = (
        "name",
        "responsible_person",
    )