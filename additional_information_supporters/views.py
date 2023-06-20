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
from .models import Additional_information_supporter
from .serializers import Additional_information_supporterDetailSerializer, Additional_information_supporterListSerializer

class Additional_information_supporters(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_additional_information_supporters = Additional_information_supporter.objects.all()
        serializer = Additional_information_supporterListSerializer(all_additional_information_supporters, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Additional_information_supporterDetailSerializer(data=request.data)
        if serializer.is_valid():
                    additional_information_supporter = serializer.save(responsible_person = request.user)   
                    serializer = Additional_information_supporterDetailSerializer(additional_information_supporter, context={"request": request},)
                    return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class Additional_information_supporterDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Additional_information_supporter.objects.get(pk=pk)
        except Additional_information_supporter.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        additional_information_supporter = self.get_object(pk)
        serializer = Additional_information_supporterDetailSerializer(additional_information_supporter, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        additional_information_supporter = self.get_object(pk)
        if additional_information_supporter.responsible_person != request.user:
            raise PermissionDenied

    def delete(self, request, pk):
        additional_information_supporter = self.get_object(pk)
        if additional_information_supporter.responsible_person != request.user:
            raise PermissionDenied
        additional_information_supporter.delete()
        return Response(status=HTTP_204_NO_CONTENT)