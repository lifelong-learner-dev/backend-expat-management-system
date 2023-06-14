import time
from django.conf import settings
from django.utils import timezone
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
from .models import Additional_information as Additional_informationModel
from .serializers import Additional_informationListSerializer, Additional_informationDetailSerializer

class Additional_information(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_additional_information = Additional_informationModel.objects.all()
        serializer = Additional_informationListSerializer(all_additional_information, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Additional_informationDetailSerializer(data=request.data)
        if serializer.is_valid():
                    additional_information = serializer.save(responsible_person = request.user)
                    serializer = Additional_informationDetailSerializer(additional_information, context={"request": request},)
                    return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class Additional_informationDetail(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Additional_informationModel.objects.get(pk=pk)
        except Additional_informationModel.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        additional_information = self.get_object(pk)
        serializer = Additional_informationDetailSerializer(additional_information, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        additional_information = self.get_object(pk)
        if additional_information.responsible_person != request.user:
            raise PermissionDenied

    def delete(self, request, pk):
        additional_information = self.get_object(pk)
        if additional_information.responsible_person != request.user:
            raise PermissionDenied
        additional_information.delete()
        return Response(status=HTTP_204_NO_CONTENT)