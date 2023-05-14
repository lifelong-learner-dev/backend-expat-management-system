from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Explanation, Moving
from users.serializers import TinyUserSerializer

class ExplanationSerializer(ModelSerializer):
    class Meta:
        model = Explanation
        fields = "__all__"

class MovingDetailSerializer(ModelSerializer):
    responsible_person = TinyUserSerializer(read_only=True)
    explanations = ExplanationSerializer(read_only=True, many=True,)

    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Moving
        fields = "__all__"

    def get_is_responsible_person(self, moving):
        request = self.context.get("request")
        if request:
            return moving.responsible_person == request.user
        return False

class MovingListSerializer(ModelSerializer):

    is_responsible_person = SerializerMethodField()

    class Meta:
        model = Moving
        fields = ("pk", "name", "subject", "responsible_person", "is_responsible_person", "explanations", "created_at", "updated_at",)

    def get_is_responsible_person(self, moving):
        request = self.context.get("request")
        return moving.responsible_person == request.user