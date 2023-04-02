from rest_framework.serializers import ModelSerializer
from .models import Explanation, Pick_up
class ExplanationSerializer(ModelSerializer):
    class Meta:
        model = Explanation
        fields = "__all__"

class Pick_upSerializer(ModelSerializer):
    class Meta:
        model = Pick_up
        fields = "__all__"