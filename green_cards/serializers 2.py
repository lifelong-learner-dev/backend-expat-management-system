from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Green_card
from users.serializers import TinyUserSerializer

class Green_cardDetailSerializer(ModelSerializer):
    expat = TinyUserSerializer(read_only=True)

    is_expat = SerializerMethodField()

    class Meta:
        model = Green_card
        fields = "__all__"

    def get_is_expat(self, green_card):
        request = self.context.get("request")
        if request:
            return green_card.expat == request.user
        return False

class Green_cardListSerializer(ModelSerializer):
    is_expat = SerializerMethodField()

    class Meta:
        model = Green_card
        fields = ("pk", "name", "expat", "is_expat", "created_at", "updated_at",)

    def get_is_expat(self, green_card):
        request = self.context.get("request")
        return green_card.expat == request.user