from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Work_permits_supporter
from users.serializers import TinyUserSerializer

class Work_permits_supporterDetailSerializer(ModelSerializer):
    responsible_person = TinyUserSerializer(read_only=True) 
    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Work_permits_supporter
        fields = "__all__"

    def get_is_responsible_person(self, work_permits_supporter):
        request = self.context.get("request")
        if request:
            return work_permits_supporter.responsible_person == request.user
        return False

class Work_permits_supporterListSerializer(ModelSerializer):

    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Work_permits_supporter
        fields = ("pk", "name", "responsible_person", "is_responsible_person", "created_at", "updated_at",)

    def get_is_responsible_person(self, work_permits_supporter):
        request = self.context.get("request")
        return work_permits_supporter.responsible_person == request.user