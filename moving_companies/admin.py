from django.contrib import admin
from .models import Moving_company

@admin.register(Moving_company)
class Moving_companyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "cellphone_number",
        "email",
        "explain",
        "detailed_information",
    )
    list_filter = (
        "name",
    )
    search_fields = (
        "name",
    )