from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomsUserAdmin(UserAdmin):
    fieldsets = (
        (
            "Profie",
            {
                "fields": ("username", 
                    "first_name", 
                    "last_name", 
                    "email",
                    "turkish_id", 
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
    list_display = ("username", "email", "first_name", "last_name", "turkish_id", "is_supporter",)