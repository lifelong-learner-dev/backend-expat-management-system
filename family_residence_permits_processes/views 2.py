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
from .models import Family_residence_permits_process
from .serializers import Family_residence_permits_processDetailSerializer, Family_residence_permits_processListSerializer

class Family_residence_permits_processes(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_family_residence_permits_processes = Family_residence_permits_process.objects.all()
        serializer = Family_residence_permits_processListSerializer(all_family_residence_permits_processes, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Family_residence_permits_processDetailSerializer(data=request.data)
        if serializer.is_valid():
                    family_residence_permits_process = serializer.save(responsible_person = request.user)   
                    serializer = Family_residence_permits_processDetailSerializer(family_residence_permits_process, context={"request": request},)
                    return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class Family_residence_permits_processDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Family_residence_permits_process.objects.get(pk=pk)
        except Family_residence_permits_process.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        family_residence_permits_process = self.get_object(pk)
        serializer = Family_residence_permits_processDetailSerializer(family_residence_permits_process, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        family_residence_permits_process = self.get_object(pk)
        if family_residence_permits_process.responsible_person != request.user:
            raise PermissionDenied

    def delete(self, request, pk):
        family_residence_permits_process = self.get_object(pk)
        if family_residence_permits_process.responsible_person != request.user:
            raise PermissionDenied
        family_residence_permits_process.delete()
        return Response(status=HTTP_204_NO_CONTENT)