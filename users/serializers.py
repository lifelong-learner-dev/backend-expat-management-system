from rest_framework.serializers import ModelSerializer
from .models import User

class TinyUserSerializer(ModelSerializer):
    class Meta: 
        model = User
        field = ("name", "avatar", "first_name", "last_name",)