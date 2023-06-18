from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Family_residence_permits_process
from users.serializers import TinyUserSerializer

class Family_residence_permits_processDetailSerializer(ModelSerializer):
    responsible_person = TinyUserSerializer(read_only=True) 
    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Family_residence_permits_process
        fields = "__all__"

    def get_is_responsible_person(self, family_residence_permits_process):
        request = self.context.get("request")
        if request:
            return family_residence_permits_process.responsible_person == request.user
        return False

class Family_residence_permits_processListSerializer(ModelSerializer):

    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Family_residence_permits_process
        fields = ("pk", "name", "responsible_person", "is_responsible_person", "created_at", "updated_at",)

    def get_is_responsible_person(self, family_residence_permits_process):
        request = self.context.get("request")
        return family_residence_permits_process.responsible_person == request.user