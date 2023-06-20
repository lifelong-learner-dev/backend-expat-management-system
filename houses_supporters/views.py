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
from .models import Houses_supporter
from .serializers import Houses_supporterDetailSerializer, Houses_supporterListSerializer

class Houses_supporters(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_houses_supporters = Houses_supporter.objects.all()
        serializer = Houses_supporterListSerializer(all_houses_supporters, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Houses_supporterDetailSerializer(data=request.data)
        if serializer.is_valid():
                    houses_supporter = serializer.save(responsible_person = request.user)   
                    serializer = Houses_supporterDetailSerializer(houses_supporter, context={"request": request},)
                    return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class Houses_supporterDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Houses_supporter.objects.get(pk=pk)
        except Houses_supporter.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        houses_supporter = self.get_object(pk)
        serializer = Houses_supporterDetailSerializer(houses_supporter, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        houses_supporter = self.get_object(pk)
        if houses_supporter.responsible_person != request.user:
            raise PermissionDenied

    def delete(self, request, pk):
        houses_supporter = self.get_object(pk)
        if houses_supporter.responsible_person != request.user:
            raise PermissionDenied
        houses_supporter.delete()
        return Response(status=HTTP_204_NO_CONTENT)