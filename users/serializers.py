from rest_framework.serializers import ModelSerializer
from .models import User

class TinyUserSerializer(ModelSerializer):
    class Meta: 
        model = User
        fields = ("first_name", "last_name", "avatar", "car_plate", "company_car_model", "car_model_year", "is_company_cars", "is_supporter", "is_manager", "is_expat", "is_director", "first_name", "last_name", "cellphone_number", "email")


class PrivateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "is_superuser",
            "id",
            "is_staff",
            "is_active",
            "groups",
            "user_permissions",
        )