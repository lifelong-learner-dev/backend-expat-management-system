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
from .models import Moving_supporter
from .serializers import Moving_supporterDetailSerializer, Moving_supporterListSerializer

class Moving_supporters(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_moving_supporters = Moving_supporter.objects.all()
        serializer = Moving_supporterListSerializer(all_moving_supporters, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Moving_supporterDetailSerializer(data=request.data)
        if serializer.is_valid():
                    moving_supporter = serializer.save(responsible_person = request.user)   
                    serializer = Moving_supporterDetailSerializer(moving_supporter, context={"request": request},)
                    return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class Moving_supporterDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Moving_supporter.objects.get(pk=pk)
        except Moving_supporter.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        moving_supporter = self.get_object(pk)
        serializer = Moving_supporterDetailSerializer(moving_supporter, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        moving_supporter = self.get_object(pk)
        if moving_supporter.responsible_person != request.user:
            raise PermissionDenied

    def delete(self, request, pk):
        moving_supporter = self.get_object(pk)
        if moving_supporter.responsible_person != request.user:
            raise PermissionDenied
        moving_supporter.delete()
        return Response(status=HTTP_204_NO_CONTENT)