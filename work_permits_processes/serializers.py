from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Work_permits_process
from users.serializers import TinyUserSerializer

class Work_permits_processDetailSerializer(ModelSerializer):

    class Meta:
        model = Work_permits_process
        fields = "__all__"

class Work_permits_processListSerializer(ModelSerializer):

    class Meta:
        model = Work_permits_process
        fields = ("pk", "name", "subject", "responsible_person_name", "is_responsible_person_name", "created_at", "updated_at",)
