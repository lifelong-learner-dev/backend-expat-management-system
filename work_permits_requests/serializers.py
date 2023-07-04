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
    expat = TinyUserSerializer(read_only=True)

    is_expat = SerializerMethodField()
    krstatus_display = SerializerMethodField(source='get_krstatus_display', read_only=True)


    class Meta:
        model = Work_permits_request
        fields = ("pk", "name", "expat", "is_expat", "location", "date", "krstatus", "krstatus_display", "created_at", "updated_at",)

    def get_is_expat(self, work_permits_request):
        request = self.context.get("request")
        return work_permits_request.expat == request.user

    def get_krstatus_display(self, work_permits_request):
        return dict(work_permits_request.KrstatusChoices.choices).get(work_permits_request.krstatus, "")