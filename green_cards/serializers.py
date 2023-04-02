from rest_framework.serializers import ModelSerializer
from .models import Explanation, Green_card
class ExplanationSerializer(ModelSerializer):
    class Meta:
        model = Explanation
        fields = "__all__"

class Green_cardSerializer(ModelSerializer):
    class Meta:
        model = Green_card
        fields = "__all__"