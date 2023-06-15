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
from .models import Green_card
from .serializers import Green_cardDetailSerializer, Green_cardListSerializer

class Green_cards(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        all_green_cards = Green_card.objects.all()
        serializer = Green_cardListSerializer(all_green_cards, many=True, context={"request": request},)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Green_cardDetailSerializer(data=request.data)
        if serializer.is_valid():
                    green_card = serializer.save(expat = request.user)   
                    serializer = Green_cardDetailSerializer(green_card, context={"request": request},)
                    return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class Green_cardDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try: 
            return Green_card.objects.get(pk=pk)
        except Green_card.DoesNotExist:
            raise NotFound
    
    def get(self, request, pk):
        green_card = self.get_object(pk)
        serializer = Green_cardDetailSerializer(green_card, context={"request": request},)
        return Response(serializer.data)

    def put(self, request, pk):
        green_card = self.get_object(pk)
        if green_card.expat != request.user:
            raise PermissionDenied

    def delete(self, request, pk):
        green_card = self.get_object(pk)
        if green_card.expat != request.user:
            raise PermissionDenied
        green_card.delete()
        return Response(status=HTTP_204_NO_CONTENT)