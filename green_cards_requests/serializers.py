from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Available_country, Green_cards_request
from users.serializers import TinyUserSerializer

class Available_countrySerializer(ModelSerializer):
    class Meta:
        model = Available_country
        fields = "__all__"

class Green_cards_requestDetailSerializer(ModelSerializer):
    expat = TinyUserSerializer(read_only=True)
    available_countries = Available_countrySerializer(read_only=True, many=True,)

    is_expat = SerializerMethodField()

    class Meta:
        model = Green_cards_request
        fields = "__all__"

    def get_is_expat(self, green_cards_request):
        request = self.context.get("request")
        if request:
            return Green_cards_request.expat == request.user
        return False

class Green_cards_requestListSerializer(ModelSerializer):

    is_expat = SerializerMethodField()

    class Meta:
        model = Green_cards_request
        fields = ("pk", "name", "expat", "is_expat", "available_countries", "create_at", "updated_at",)

    def get_is_expat(self, green_cards_request):
        request = self.context.get("request")
        return green_cards_request.expat == request.user