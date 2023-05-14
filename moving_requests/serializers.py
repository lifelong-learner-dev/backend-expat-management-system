from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Moving_request
from users.serializers import TinyUserSerializer

class Moving_requestDetailSerializer(ModelSerializer):
    expat = TinyUserSerializer(read_only=True)

    is_expat = SerializerMethodField()

    class Meta:
        model = Moving_request
        fields = "__all__"

    def get_is_expat(self, moving_request):
        request = self.context.get("request")
        if request:
            return Moving_request.expat == request.user
        return False

class Moving_requestListSerializer(ModelSerializer):

    is_expat = SerializerMethodField()

    class Meta:
        model = Moving_request
        fields = ("pk", "name", "expat", "is_expat", "create_at", "updated_at",)

    def get_is_expat(self, moving_request):
        request = self.context.get("request")
        return moving_request.expat == request.user