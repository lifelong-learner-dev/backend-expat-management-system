from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Work_permit

@api_view()
def work_permits(request):
    return Response({
        "ok": True,
    })
