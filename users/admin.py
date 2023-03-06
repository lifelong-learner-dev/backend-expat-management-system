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
                    "first_name", 
                    "last_name", 
                    "email",
                    "house_address",
                    "company_car_model",
                    "car_plate",
                    "turkish_id",
                    "tc_id_expiry_date",
                    "passport_number",
                    "passport_expiry_date",
                    "is_supporter", 
                    "gender", 
                    "language", 
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
    list_display = ("username", "email", "first_name", "last_name", "company_car_model", "car_plate", "house_address", "turkish_id", "tc_id_expiry_date", "passport_number", "passport_expiry_date", "is_supporter")