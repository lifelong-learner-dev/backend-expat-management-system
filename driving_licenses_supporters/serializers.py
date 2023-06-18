from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Driving_licenses_supporter
from users.serializers import TinyUserSerializer

class Driving_licenses_supporterDetailSerializer(ModelSerializer):
    class Meta:
        model = Driving_licenses_supporter
        fields = "__all__"

class Driving_licenses_supporterListSerializer(ModelSerializer):

    class Meta:
        model = Driving_licenses_supporter
        fields = ("pk", "name", "created_at", "updated_at",)