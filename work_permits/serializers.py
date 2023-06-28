from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Work_permit
from users.serializers import TinyUserSerializer

class Work_permitDetailSerializer(ModelSerializer):
    expat = TinyUserSerializer(read_only=True)

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
    expat = TinyUserSerializer(read_only=True)
    is_expat = SerializerMethodField()
    krstatus_display = SerializerMethodField(source='get_krstatus_display', read_only=True)

    class Meta:
        model = Work_permit
        fields = ("pk", "name", "expat", "is_expat", "krstatus", "krstatus_display", "enstatus", "created_at", "updated_at",)

    def get_is_expat(self, work_permit):
        request = self.context.get("request")
        return work_permit.expat == request.user

    def get_krstatus_display(self, work_permit):
        return dict(work_permit.KrstatusChoices.choices).get(work_permit.krstatus, "")