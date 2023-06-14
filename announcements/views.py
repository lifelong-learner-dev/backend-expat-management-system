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
from .models import Announcement
from .serializers import AnnouncementDetailSerializer, AnnouncementListSerializer

class Announcements(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_announcements = Announcement.objects.all()
        serializer = AnnouncementListSerializer(all_announcements, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AnnouncementDetailSerializer(data=request.data)
        if serializer.is_valid():
                    announcement = serializer.save(responsible_person = request.user)    
                    serializer = AnnouncementDetailSerializer(announcement, context={"request": request},)
                    return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    

class AnnouncementDetail(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Announcement.objects.get(pk=pk)
        except Announcement.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        announcement = self.get_object(pk)
        serializer = AnnouncementDetailSerializer(announcement, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        announcement = self.get_object(pk)
        if announcement.responsible_person != request.user:
            raise PermissionDenied

    def delete(self, request, pk):
        announcement = self.get_object(pk)
        if announcement.responsible_person != request.user:
            raise PermissionDenied
        announcement.delete()
        return Response(status=HTTP_204_NO_CONTENT)