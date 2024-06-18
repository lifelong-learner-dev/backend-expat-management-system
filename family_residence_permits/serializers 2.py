from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Family_residence_permit
from users.serializers import TinyUserSerializer

class Family_residence_permitDetailSerializer(ModelSerializer):
    expat = TinyUserSerializer(read_only=True)

    is_expat = SerializerMethodField()

    class Meta:
        model = Family_residence_permit
        fields = "__all__"

    def get_is_expat(self, family_residence_permit):
        request = self.context.get("request")
        if request:
            return family_residence_permit.expat == request.user
        return False


class Family_residence_permitListSerializer(ModelSerializer):

    is_expat = SerializerMethodField()

    class Meta:
        model = Family_residence_permit
        fields = ("pk", "name", "expat", "is_expat", "created_at", "updated_at",)

    def get_is_expat(self, family_residence_permit):
        request = self.context.get("request")
        return family_residence_permit.expat == request.user