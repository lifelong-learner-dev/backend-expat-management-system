from rest_framework.serializers import ModelSerializer
from .models import Available_country, Green_cards_request
class Available_countrySerializer(ModelSerializer):
    class Meta:
        model = Available_country
        fields = "__all__"

class Green_cards_requestSerializer(ModelSerializer):
    class Meta:
        model = Green_cards_request
        fields = "__all__"