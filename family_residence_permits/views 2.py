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
from .models import Family_residence_permit
from .serializers import Family_residence_permitDetailSerializer, Family_residence_permitListSerializer

class Family_residence_permits(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_family_residence_permits = Family_residence_permit.objects.all()
        serializer = Family_residence_permitListSerializer(all_family_residence_permits, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Family_residence_permitDetailSerializer(data=request.data)
        if serializer.is_valid():
                    family_residence_permit = serializer.save(expat = request.user) 
                    serializer = Family_residence_permitDetailSerializer(family_residence_permit, context={"request": request},)
                    return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class Family_residence_permitDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Family_residence_permit.objects.get(pk=pk)
        except Family_residence_permit.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        family_residence_permit = self.get_object(pk)
        serializer = Family_residence_permitDetailSerializer(family_residence_permit, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        family_residence_permit = self.get_object(pk)
        if not family_residence_permit.expat == request.user or not request.user.is_supporter and not request.user.is_family_residence_permits:
            raise PermissionDenied

    def delete(self, request, pk):
        family_residence_permit = self.get_object(pk)
        if not family_residence_permit.expat == request.user or not request.user.is_supporter and not request.user.is_family_residence_permits:
            raise PermissionDenied
        family_residence_permit.delete()
        return Response(status=HTTP_204_NO_CONTENT)