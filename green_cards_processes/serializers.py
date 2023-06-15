from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Green_cards_process
from users.serializers import TinyUserSerializer

class Green_cards_processDetailSerializer(ModelSerializer):
    responsible_person = TinyUserSerializer(read_only=True) 
    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Green_cards_process
        fields = "__all__"

    def get_is_responsible_person(self, green_cards_process):
        request = self.context.get("request")
        if request:
            return green_cards_process.responsible_person == request.user
        return False

class Green_cards_processListSerializer(ModelSerializer):

    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Green_cards_process
        fields = ("pk", "name", "responsible_person", "is_responsible_person", "created_at", "updated_at",)

    def get_is_responsible_person(self, green_cards_process):
        request = self.context.get("request")
        return green_cards_process.responsible_person == request.user