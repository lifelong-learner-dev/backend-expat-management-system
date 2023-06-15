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
from .models import Driving_licenses_process
from .serializers import Driving_licenses_processDetailSerializer, Driving_licenses_processListSerializer

class Driving_licenses_processes(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_driving_licenses_processes = Driving_licenses_process.objects.all()
        serializer = Driving_licenses_processListSerializer(all_driving_licenses_processes, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Driving_licenses_processDetailSerializer(data=request.data)
        if serializer.is_valid():
                    driving_licenses_process = serializer.save(responsible_person = request.user)   
                    serializer = Driving_licenses_processDetailSerializer(driving_licenses_process, context={"request": request},)
                    return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class Driving_licenses_processDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Driving_licenses_process.objects.get(pk=pk)
        except Driving_licenses_process.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        driving_licenses_process = self.get_object(pk)
        serializer = Driving_licenses_processDetailSerializer(driving_licenses_process, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        driving_licenses_process = self.get_object(pk)
        if driving_licenses_process.responsible_person != request.user:
            raise PermissionDenied

    def delete(self, request, pk):
        driving_licenses_process = self.get_object(pk)
        if driving_licenses_process.responsible_person != request.user:
            raise PermissionDenied
        driving_licenses_process.delete()
        return Response(status=HTTP_204_NO_CONTENT)