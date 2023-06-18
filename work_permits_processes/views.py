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
from .models import Work_permits_process
from .serializers import Work_permits_processDetailSerializer, Work_permits_processListSerializer

class Work_permits_processes(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_work_permits_processes = Work_permits_process.objects.all()
        serializer = Work_permits_processListSerializer(all_work_permits_processes, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Work_permits_processDetailSerializer(data=request.data)
        if request.user.is_support and request.user.is_houses and serializer.is_valid():
                    work_permits_process = serializer.save()   
                    serializer = Work_permits_processDetailSerializer(work_permits_process, context={"request": request},)
                    return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class Work_permits_processDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Work_permits_process.objects.get(pk=pk)
        except Work_permits_process.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        work_permits_process = self.get_object(pk)
        serializer = Work_permits_processDetailSerializer(work_permits_process, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        work_permits_process = self.get_object(pk)
        if not request.user.is_supporter and not request.user.is_houses:
            raise PermissionDenied
        return Response()

    def delete(self, request, pk):
        work_permits_process = self.get_object(pk)
        if not request.user.is_supporter and not request.user.is_houses:
            raise PermissionDenied
        work_permits_process.delete()
        return Response(status=HTTP_204_NO_CONTENT)