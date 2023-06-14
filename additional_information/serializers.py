from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Additional_information
from users.serializers import TinyUserSerializer

class Additional_informationDetailSerializer(ModelSerializer):
    responsible_person = TinyUserSerializer(read_only=True)

    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Additional_information
        fields = "__all__"

    def get_is_responsible_person(self, additional_information):
        request = self.context.get("request")
        if request:
            return additional_information.responsible_person == request.user
        return False

class Additional_informationListSerializer(ModelSerializer):

    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Additional_information
        fields = ("pk", "name", "subject", "responsible_person", "is_responsible_person", "created_at", "updated_at",)

    def get_is_responsible_person(self, additional_information):
        request = self.context.get("request")
        return additional_information.responsible_person == request.user