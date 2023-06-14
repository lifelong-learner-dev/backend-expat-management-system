from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Real_estate_agent
from users.serializers import TinyUserSerializer

class Real_estate_agentDetailSerializer(ModelSerializer):

    class Meta:
        model = Real_estate_agent
        fields = "__all__"

class Real_estate_agentListSerializer(ModelSerializer):

    class Meta:
        model = Real_estate_agent
        fields = ("pk", "name", "subject", "responsible_person_name", "is_responsible_person_name", "created_at", "updated_at",)
