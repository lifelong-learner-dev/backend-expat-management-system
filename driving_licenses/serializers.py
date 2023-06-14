from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Driving_license
from users.serializers import TinyUserSerializer

class Driving_licenseDetailSerializer(ModelSerializer):
    expat = TinyUserSerializer(read_only=True)
    is_expat = SerializerMethodField()

    class Meta:
        model = Driving_license
        fields = "__all__"

    def get_is_expat(self, driving_license):
        request = self.context.get("request")
        if request:
            return driving_license.expat == request.user
        return False

class Driving_licenseListSerializer(ModelSerializer):

    is_expat = SerializerMethodField()

    class Meta:
        model = Driving_license
        fields = ("pk", "name", "expat", "is_expat", "created_at", "updated_at",)

    def get_is_expat(self, driving_license):
        request = self.context.get("request")
        return driving_license.expat == request.user