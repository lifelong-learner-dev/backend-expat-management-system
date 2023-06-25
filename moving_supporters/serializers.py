from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Moving_supporter
from users.serializers import TinyUserSerializer

class Moving_supporterDetailSerializer(ModelSerializer):
    responsible_person = TinyUserSerializer(read_only=True) 
    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Moving_supporter
        fields = "__all__"

    def get_is_responsible_person(self, moving_supporter):
        request = self.context.get("request")
        if request:
            return moving_supporter.responsible_person == request.user
        return False

class Moving_supporterListSerializer(ModelSerializer):

    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Moving_supporter
        fields = ("pk", "name", "responsible_person", "is_responsible_person", "created_at", "updated_at",)

    def get_is_responsible_person(self, moving_supporter):
        request = self.context.get("request")
        return moving_supporter.responsible_person == request.user