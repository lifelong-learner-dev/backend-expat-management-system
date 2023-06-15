from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Family_residence_permits_request
from users.serializers import TinyUserSerializer


class Family_residence_permits_requestDetailSerializer(ModelSerializer):
    expat = TinyUserSerializer(read_only=True)

    is_expat = SerializerMethodField()

    class Meta:
        model = Family_residence_permits_request
        fields = "__all__"

    def get_is_expat(self, family_residence_permits_request):
        request = self.context.get("request")
        if request:
            return Family_residence_permits_request.expat == request.user
        return False

class Family_residence_permits_requestListSerializer(ModelSerializer):

    is_expat = SerializerMethodField()

    class Meta:
        model = Family_residence_permits_request
        fields = ("pk", "name", "expat", "is_expat", "create_at", "updated_at",)

    def get_is_expat(self, family_residence_permits_request):
        request = self.context.get("request")
        return family_residence_permits_request.expat == request.user