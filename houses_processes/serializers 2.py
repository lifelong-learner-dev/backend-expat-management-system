from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Houses_process
from users.serializers import TinyUserSerializer

class Houses_processDetailSerializer(ModelSerializer):
    responsible_person = TinyUserSerializer(read_only=True) 
    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Houses_process
        fields = "__all__"

    def get_is_responsible_person(self, houses_process):
        request = self.context.get("request")
        if request:
            return houses_process.responsible_person == request.user
        return False

class Houses_processListSerializer(ModelSerializer):

    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Houses_process
        fields = ("pk", "name", "responsible_person", "is_responsible_person", "created_at", "updated_at",)

    def get_is_responsible_person(self, houses_process):
        request = self.context.get("request")
        return houses_process.responsible_person == request.user