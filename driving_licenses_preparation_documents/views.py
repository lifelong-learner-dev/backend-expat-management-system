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
from .models import Driving_licenses_preparation_document
from .serializers import Driving_licenses_preparation_documentDetailSerializer, Driving_licenses_preparation_documentListSerializer

class Driving_licenses_preparation_documents(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_driving_licenses_preparation_documents = Driving_licenses_preparation_document.objects.all()
        serializer = Driving_licenses_preparation_documentListSerializer(all_driving_licenses_preparation_documents, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Driving_licenses_preparation_documentDetailSerializer(data=request.data)
        if request.user.is_supporter and request.user.is_driving_licenses and serializer.is_valid():
            driving_licenses_preparation_document = serializer.save(expat = request.user)
            serializer = Driving_licenses_preparation_documentDetailSerializer(driving_licenses_preparation_document, context={"request": request},)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class Driving_licenses_preparation_documentDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Driving_licenses_preparation_document.objects.get(pk=pk)
        except Driving_licenses_preparation_document.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        driving_licenses_preparation_document = self.get_object(pk)
        serializer = Driving_licenses_preparation_documentDetailSerializer(driving_licenses_preparation_document, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        driving_licenses_preparation_document = self.get_object(pk)
        serializer = Driving_licenses_preparation_documentDetailSerializer(driving_licenses_preparation_document, data=request.data, partial=True)
        if request.user.is_supporter and request.user.is_driving_licenses and serializer.is_valid():
            updated_driving_licenses_preparation_document = serializer.save()
            return Response(Driving_licenses_preparation_documentDetailSerializer(updated_driving_licenses_preparation_document).data,)
        else:
          raise PermissionDenied

    def delete(self, request, pk):
        driving_licenses_preparation_document = self.get_object(pk)
        if not request.user.is_supporter and request.user.is_driving_licenses:
            raise PermissionDenied
        driving_licenses_preparation_document.delete()
        return Response(status=HTTP_204_NO_CONTENT)