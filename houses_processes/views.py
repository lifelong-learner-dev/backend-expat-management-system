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
from .models import Houses_process
from .serializers import Houses_processDetailSerializer, Houses_processListSerializer

class Houses_processes(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_houses_processes = Houses_process.objects.all()
        serializer = Houses_processListSerializer(all_houses_processes, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Houses_processDetailSerializer(data=request.data)
        if serializer.is_valid():
                    houses_process = serializer.save(responsible_person = request.user)   
                    serializer = Houses_processDetailSerializer(houses_process, context={"request": request},)
                    return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class Houses_processDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Houses_process.objects.get(pk=pk)
        except Houses_process.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        houses_process = self.get_object(pk)
        serializer = Houses_processDetailSerializer(houses_process, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        houses_process = self.get_object(pk)
        if houses_process.responsible_person != request.user:
            raise PermissionDenied

    def delete(self, request, pk):
        houses_process = self.get_object(pk)
        if houses_process.responsible_person != request.user:
            raise PermissionDenied
        houses_process.delete()
        return Response(status=HTTP_204_NO_CONTENT)