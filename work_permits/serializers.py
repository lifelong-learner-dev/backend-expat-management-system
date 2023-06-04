from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Explanation, Work_permit
from users.serializers import TinyUserSerializer

class ExplanationSerializer(ModelSerializer):
    class Meta:
        model = Explanation
        fields = "__all__"

class Work_permitDetailSerializer(ModelSerializer):
    expat = TinyUserSerializer(read_only=True)
    explanations = ExplanationSerializer(read_only=True, many=True,)

    is_expat = SerializerMethodField()

    class Meta:
        model = Work_permit
        fields = "__all__"

    def get_is_expat(self, work_permit):
        request = self.context.get("request")
        if request:
            return work_permit.expat == request.user
        return False

class Work_permitListSerializer(ModelSerializer):
    is_expat = SerializerMethodField()

    class Meta:
        model = Work_permit
        fields = ("pk", "name", "expat", "is_expat", "explanations", "created_at", "updated_at",)

    def get_is_expat(self, work_permit):
        request = self.context.get("request")
        return work_permit.expat == request.user