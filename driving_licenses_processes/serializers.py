from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Driving_licenses_process
from users.serializers import TinyUserSerializer

class Driving_licenses_processDetailSerializer(ModelSerializer):
    responsible_person = TinyUserSerializer(read_only=True) 
    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Driving_licenses_process
        fields = "__all__"

    def get_is_responsible_person(self, driving_licenses_process):
        request = self.context.get("request")
        if request:
            return driving_licenses_process.responsible_person == request.user
        return False

class Driving_licenses_processListSerializer(ModelSerializer):

    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Driving_licenses_process
        fields = ("pk", "name", "responsible_person", "is_responsible_person", "created_at", "updated_at",)

    def get_is_responsible_person(self, driving_licenses_process):
        request = self.context.get("request")
        return driving_licenses_process.responsible_person == request.user