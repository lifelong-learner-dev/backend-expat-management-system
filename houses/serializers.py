from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import House
from users.serializers import TinyUserSerializer


class HouseDetailSerializer(ModelSerializer):
    responsible_person = TinyUserSerializer(read_only=True)

    is_responsible_person = SerializerMethodField()

    class Meta:
        model = House
        fields = "__all__"

    def get_is_responsible_person(self, house):
        request = self.context.get("request")
        if request:
            return house.responsible_person == request.user
        return False


class HouseListSerializer(ModelSerializer):

    is_responsible_person = SerializerMethodField()

    class Meta:
        model = House
        fields = ("pk", "name", "subject", "responsible_person", "is_responsible_person", "created_at", "updated_at",)

    def get_is_responsible_person(self, house):
        request = self.context.get("request")
        return house.responsible_person == request.user