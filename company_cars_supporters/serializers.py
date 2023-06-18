from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Company_cars_supporter
from users.serializers import TinyUserSerializer

class Company_cars_supporterDetailSerializer(ModelSerializer):

    class Meta:
        model = Company_cars_supporter
        fields = "__all__"


class Company_cars_supporterListSerializer(ModelSerializer):

    class Meta:
        model = Company_cars_supporter
        fields = ("pk", "name", "created_at", "updated_at",)
