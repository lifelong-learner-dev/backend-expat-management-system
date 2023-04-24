from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomsUserAdmin(UserAdmin):
    fieldsets = (
        (
            "Profile",
            {
                "fields": ("username",
                    "avatar",
                    "division",
                    "department",
                    "position",
                    "hq_position",
                    "first_name", 
                    "last_name", 
                    "cellphone_number",
                    "email",
                    "house_address",
                    "company_car_model",
                    "car_plate",
                    "car_model_year", 
                    "car_location",
                    "turkish_id",
                    "tc_id_expiry_date",
                    "passport_number",
                    "passport_expiry_date",
                    "is_manager",
                    "is_expat",
                    "is_supporter",
                    "is_director", 
                    "gender", 
                    "language", 
                    "is_company_cars",
                    "is_driving_licenses",
                    "is_family_residence_permits",
                    "is_green_cards",
                    "is_houses",
                    "is_moving",
                    "is_pick_ups",
                    "is_work_permits",
                    "house_location",
                    "currency"),
                },
        ),
        ("Permissions", 
            {
                "fields": (  
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", 
            {
                "fields": (
                    "last_login", "date_joined",
                    ),
            },
        ),
    )    
    list_display = ("username", "division", "department", "position", "hq_position", "company_car_model", "car_plate", "house_address", "turkish_id", "tc_id_expiry_date", "passport_number", "passport_expiry_date", )