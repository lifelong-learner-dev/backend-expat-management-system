from django.contrib import admin
from .models import Company_cars_supporter

@admin.register(Company_cars_supporter)
class Company_cars_supporterAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created_at",
    )

    list_filter = (
        "name",
    )
    search_fields = (
        "name",
    )