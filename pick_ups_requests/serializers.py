from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Pick_ups_request
from users.serializers import TinyUserSerializer

class Pick_ups_requestDetailSerializer(ModelSerializer):
    expat = TinyUserSerializer(read_only=True)

    is_expat = SerializerMethodField()

    class Meta:
        model = Pick_ups_request
        fields = "__all__"

    def get_is_expat(self, pick_ups_request):
        request = self.context.get("request")
        if request:
            return Pick_ups_request.expat == request.user
        return False

class Pick_ups_requestListSerializer(ModelSerializer):

    is_expat = SerializerMethodField()

    class Meta:
        model = Pick_ups_request
        fields = ("pk", "name", "expat", "is_expat", "create_at", "updated_at",)

    def get_is_expat(self, pick_ups_request):
        request = self.context.get("request")
        return pick_ups_request.expat == request.user