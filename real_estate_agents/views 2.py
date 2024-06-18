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
from .models import Real_estate_agent
from .serializers import Real_estate_agentDetailSerializer, Real_estate_agentListSerializer

class Real_estate_agents(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_real_estate_agents = Real_estate_agent.objects.all()
        serializer = Real_estate_agentListSerializer(all_real_estate_agents, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Real_estate_agentDetailSerializer(data=request.data)
        if request.user.is_support and request.user.is_houses and serializer.is_valid():
                    real_estate_agent = serializer.save()   
                    serializer = Real_estate_agentDetailSerializer(real_estate_agent, context={"request": request},)
                    return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class Real_estate_agentDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Real_estate_agent.objects.get(pk=pk)
        except Real_estate_agent.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        real_estate_agent = self.get_object(pk)
        serializer = Real_estate_agentDetailSerializer(real_estate_agent, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        real_estate_agent = self.get_object(pk)
        if not request.user.is_supporter and not request.user.is_houses:
            raise PermissionDenied
        return Response()

    def delete(self, request, pk):
        real_estate_agent = self.get_object(pk)
        if not request.user.is_supporter and not request.user.is_houses:
            raise PermissionDenied
        real_estate_agent.delete()
        return Response(status=HTTP_204_NO_CONTENT)