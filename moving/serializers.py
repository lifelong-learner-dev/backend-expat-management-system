from rest_framework.serializers import ModelSerializer
from .models import Explanation, Moving
class ExplanationSerializer(ModelSerializer):
    class Meta:
        model = Explanation
        fields = "__all__"

class MovingSerializer(ModelSerializer):
    class Meta:
        model = Moving
        fields = "__all__"