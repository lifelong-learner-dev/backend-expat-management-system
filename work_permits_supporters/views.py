import time
from django.conf import settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    ParseError,
    PermissionDenied,
)
from .models import Work_permits_supporter
from .serializers import Work_permits_supporterDetailSerializer, Work_permits_supporterListSerializer

class Work_permits_supporters(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_work_permits_supporters = Work_permits_supporter.objects.all()
        serializer = Work_permits_supporterListSerializer(all_work_permits_supporters, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Work_permits_supporterDetailSerializer(data=request.data)
        if serializer.is_valid():
                    work_permits_supporter = serializer.save(responsible_person = request.user)   
                    serializer = Work_permits_supporterDetailSerializer(work_permits_supporter, context={"request": request},)
                    return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class Work_permits_supporterDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Work_permits_supporter.objects.get(pk=pk)
        except Work_permits_supporter.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        work_permits_supporter = self.get_object(pk)
        serializer = Work_permits_supporterDetailSerializer(work_permits_supporter, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        work_permits_supporter = self.get_object(pk)
        if work_permits_supporter.responsible_person != request.user:
            raise PermissionDenied

    def delete(self, request, pk):
        work_permits_supporter = self.get_object(pk)
        if work_permits_supporter.responsible_person != request.user:
            raise PermissionDenied
        work_permits_supporter.delete()
        return Response(status=HTTP_204_NO_CONTENT)