from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Explanation, Pick_up
from users.serializers import TinyUserSerializer

class ExplanationSerializer(ModelSerializer):
    class Meta:
        model = Explanation
        fields = "__all__"

class Pick_upDetailSerializer(ModelSerializer):
    expat = TinyUserSerializer(read_only=True)
    explanations = ExplanationSerializer(read_only=True, many=True,)

    is_expat = SerializerMethodField()

    class Meta:
        model = Pick_up
        fields = "__all__"

    def get_is_expat(self, pick_up):
        request = self.context.get("request")
        if request:
            return pick_up.expat == request.user
        return False

class Pick_upListSerializer(ModelSerializer):
    is_expat = SerializerMethodField()

    class Meta:
        model = Pick_up
        fields = ("pk", "name", "expat", "is_expat", "explanations", "created_at", "updated_at",)

    def get_is_expat(self, pick_up):
        request = self.context.get("request")
        return pick_up.expat == request.user