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
from .models import Family_residence_permits_processes_supporter
from .serializers import Family_residence_permits_processes_supporterDetailSerializer, Family_residence_permits_processes_supporterListSerializer

class Family_residence_permits_processes_supporters(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_family_residence_permits_processes_supporters = Family_residence_permits_processes_supporter.objects.all()
        serializer = Family_residence_permits_processes_supporterListSerializer(all_family_residence_permits_processes_supporters, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Family_residence_permits_processes_supporterDetailSerializer(data=request.data)
        if serializer.is_valid():
                    family_residence_permits_processes_supporter = serializer.save(responsible_person = request.user)   
                    serializer = Family_residence_permits_processes_supporterDetailSerializer(family_residence_permits_processes_supporter, context={"request": request},)
                    return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class Family_residence_permits_processes_supporterDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Family_residence_permits_processes_supporter.objects.get(pk=pk)
        except Family_residence_permits_processes_supporter.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        family_residence_permits_processes_supporter = self.get_object(pk)
        serializer = Family_residence_permits_processes_supporterDetailSerializer(family_residence_permits_processes_supporter, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        family_residence_permits_processes_supporter = self.get_object(pk)
        if family_residence_permits_processes_supporter.responsible_person != request.user:
            raise PermissionDenied

    def delete(self, request, pk):
        family_residence_permits_processes_supporter = self.get_object(pk)
        if family_residence_permits_processes_supporter.responsible_person != request.user:
            raise PermissionDenied
        family_residence_permits_processes_supporter.delete()
        return Response(status=HTTP_204_NO_CONTENT)
