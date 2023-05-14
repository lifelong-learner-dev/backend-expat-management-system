from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Work_permits_request
from users.serializers import TinyUserSerializer

class Work_permits_requestDetailSerializer(ModelSerializer):
    expat = TinyUserSerializer(read_only=True)

    is_expat = SerializerMethodField()

    class Meta:
        model = Work_permits_request
        fields = "__all__"

    def get_is_expat(self, work_permits_request):
        request = self.context.get("request")
        if request:
            return Work_permits_request.expat == request.user
        return False

class Work_permits_requestListSerializer(ModelSerializer):

    is_expat = SerializerMethodField()

    class Meta:
        model = Work_permits_request
        fields = ("pk", "name", "expat", "is_expat", "create_at", "updated_at",)

    def get_is_expat(self, work_permits_request):
        request = self.context.get("request")
        return work_permits_request.expat == request.user