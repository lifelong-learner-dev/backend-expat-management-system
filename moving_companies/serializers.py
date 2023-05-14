from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Moving_company
from users.serializers import TinyUserSerializer

class Moving_companyDetailSerializer(ModelSerializer):

    class Meta:
        model = Moving_company
        fields = "__all__"

class Moving_companyListSerializer(ModelSerializer):

    class Meta:
        model = Moving_company
        fields = ("pk", "name", "subject", "responsible_person", "is_responsible_person", "created_at", "updated_at",)
