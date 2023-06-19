from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Driving_licenses_supporter
from users.serializers import TinyUserSerializer

class Driving_licenses_supporterDetailSerializer(ModelSerializer):
    responsible_person = TinyUserSerializer(read_only=True) 
    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Driving_licenses_supporter
        fields = "__all__"

    def get_is_responsible_person(self, driving_licenses_supporter):
        request = self.context.get("request")
        if request:
            return driving_licenses_supporter.responsible_person == request.user
        return False

class Driving_licenses_supporterListSerializer(ModelSerializer):

    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Driving_licenses_supporter
        fields = ("pk", "name", "responsible_person", "is_responsible_person", "created_at", "updated_at",)

    def get_is_responsible_person(self, driving_licenses_supporter):
        request = self.context.get("request")
        return driving_licenses_supporter.responsible_person == request.user