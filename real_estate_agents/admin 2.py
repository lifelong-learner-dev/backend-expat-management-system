from django.contrib import admin
from .models import Real_estate_agent

@admin.register(Real_estate_agent)
class Real_estate_agentAdmin(admin.ModelAdmin):
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