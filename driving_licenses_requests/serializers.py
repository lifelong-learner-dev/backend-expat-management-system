from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Driving_licenses_request
from users.serializers import TinyUserSerializer


class Driving_licenses_requestDetailSerializer(ModelSerializer):
    expat = TinyUserSerializer(read_only=True)

    is_expat = SerializerMethodField()

    class Meta:
        model = Driving_licenses_request
        fields = "__all__"

    def get_is_expat(self, driving_licenses_request):
        request = self.context.get("request")
        if request:
            return driving_licenses_request.expat == request.user
        return False

class Driving_licenses_requestListSerializer(ModelSerializer):

    is_expat = SerializerMethodField()

    class Meta:
        model = Driving_licenses_request
        fields = ("pk", "name", "expat", "is_expat", "created_at", "updated_at",)

    def get_is_expat(self, driving_licenses_request):
        request = self.context.get("request")
        return driving_licenses_request.expat == request.user