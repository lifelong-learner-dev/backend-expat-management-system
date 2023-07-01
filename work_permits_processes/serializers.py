from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Work_permits_process
from users.serializers import TinyUserSerializer

class Work_permits_processDetailSerializer(ModelSerializer):
    responsible_person = TinyUserSerializer(read_only=True)
    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Work_permits_process
        fields = "__all__"

    def get_is_responsible_person(self, work_permits_process):
        request = self.context.get("request")
        if request:
            return work_permits_process.responsible_person == request.user
        return False

class Work_permits_processListSerializer(ModelSerializer):
    responsible_person = TinyUserSerializer(read_only=True)
    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Work_permits_process
        fields = "__all__"

    def get_is_responsible_person(self, work_permits_process):
        request = self.context.get("request")
        return work_permits_process.responsible_person == request.user