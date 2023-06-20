from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Houses_supporter
from users.serializers import TinyUserSerializer

class Houses_supporterDetailSerializer(ModelSerializer):
    responsible_person = TinyUserSerializer(read_only=True) 
    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Houses_supporter
        fields = "__all__"

    def get_is_responsible_person(self, houses_supporter):
        request = self.context.get("request")
        if request:
            return houses_supporter.responsible_person == request.user
        return False

class Houses_supporterListSerializer(ModelSerializer):

    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Houses_supporter
        fields = ("pk", "name", "responsible_person", "is_responsible_person", "created_at", "updated_at",)

    def get_is_responsible_person(self, houses_supporter):
        request = self.context.get("request")
        return houses_supporter.responsible_person == request.user