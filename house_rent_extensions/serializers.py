from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import House_rent_extension
from users.serializers import TinyUserSerializer

class House_rent_extensionDetailSerializer(ModelSerializer):
    responsible_person = TinyUserSerializer(read_only=True)

    is_responsible_person = SerializerMethodField()

    class Meta:
        model = House_rent_extension
        fields = "__all__"

    def get_is_responsible_person(self, house_rent_extension):
        request = self.context.get("request")
        if request:
            return house_rent_extension.responsible_person == request.user
        return False

class House_rent_extensionListSerializer(ModelSerializer):

    is_responsible_person = SerializerMethodField()

    class Meta:
        model = House_rent_extension
        fields = ("pk", "name", "subject", "responsible_person", "is_responsible_person", "created_at", "updated_at",)

    def get_is_responsible_person(self, house_rent_extension):
        request = self.context.get("request")
        return house_rent_extension.responsible_person == request.user