from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Additional_information_supporter
from users.serializers import TinyUserSerializer

class Additional_information_supporterDetailSerializer(ModelSerializer):
    responsible_person = TinyUserSerializer(read_only=True) 
    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Additional_information_supporter
        fields = "__all__"

    def get_is_responsible_person(self, additional_information_supporter):
        request = self.context.get("request")
        if request:
            return additional_information_supporter.responsible_person == request.user
        return False

class Additional_information_supporterListSerializer(ModelSerializer):

    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Additional_information_supporter
        fields = ("pk", "name", "responsible_person", "is_responsible_person", "created_at", "updated_at",)

    def get_is_responsible_person(self, additional_information_supporter):
        request = self.context.get("request")
        return additional_information_supporter.responsible_person == request.user